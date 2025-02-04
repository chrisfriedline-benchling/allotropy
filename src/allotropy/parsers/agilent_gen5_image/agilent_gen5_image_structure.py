from __future__ import annotations

from collections import defaultdict
from collections.abc import Iterator
from dataclasses import dataclass
from io import StringIO
import re

from allotropy.allotrope.models.adm.plate_reader.benchling._2023._09.plate_reader import (
    TransmittedLightSetting,
)
from allotropy.allotrope.models.shared.definitions.units import UNITLESS
from allotropy.allotrope.schema_mappers.adm.plate_reader.benchling._2023._09.plate_reader import (
    ImageFeature,
    Measurement,
    MeasurementGroup,
    MeasurementType,
    Metadata,
    ProcessedData,
)
from allotropy.exceptions import (
    AllotropeConversionError,
)
from allotropy.parsers.agilent_gen5.agilent_gen5_structure import HeaderData
from allotropy.parsers.agilent_gen5_image.constants import (
    AUTOFOCUS_STRINGS,
    CHANNEL_HEADER_REGEX,
    DEFAULT_SOFTWARE_NAME,
    DETECTION_TYPE,
    DetectionType,
    DETECTOR_DISTANCE_REGEX,
    DEVICE_TYPE,
    METADATA_ONLY,
    ReadType,
    SETTINGS_SECTION_REGEX,
    TRANSMITTED_LIGHT_MAP,
    UNSUPPORTED_READ_TYPE_ERROR,
)
from allotropy.parsers.constants import NOT_APPLICABLE
from allotropy.parsers.lines_reader import LinesReader, SectionLinesReader
from allotropy.parsers.utils.pandas import read_csv
from allotropy.parsers.utils.uuids import random_uuid_str
from allotropy.parsers.utils.values import (
    try_float,
    try_float_or_nan,
    try_float_or_none,
)


def parse_settings(settings: list[str]) -> tuple[dict[str, str], list[str]]:
    """Returns a dictionary containing all key values identified in a list of settings.

    If there are additional (non key value) settings, they are also returned under the
    'non_kv_settings' key.

    Supported settings lines format:
        - key: value -> returned as {'key': 'value'}
        - key1: value1, key2: value2, ... -> returned as {'key1': 'value1', key2', 'value2', ...}
        - Non keyvalue setting -> returned as {'non_kv_settings': ['Non keyvalue setting', ...]}
    """
    non_kv_settings: list[str] = []
    settings_dict: dict[str, str] = {}
    for line in settings:
        strp_line = str(line.strip())

        line_data: list[str] = strp_line.split(", ")
        for read_datum in line_data:
            splitted_datum = read_datum.split(": ")
            if len(splitted_datum) == 1:
                non_kv_settings.append(splitted_datum[0])
            elif len(splitted_datum) == 2:
                settings_dict[splitted_datum[0]] = splitted_datum[1]

    return settings_dict, non_kv_settings


@dataclass
class InstrumentSettings:
    auto_focus: bool
    detector_distance: float | None
    fluorescent_tag: str | None = None
    excitation_wavelength: float | None = None
    detector_wavelength: float | None = None
    transmitted_light: TransmittedLightSetting | None = None
    illumination: float | None = None
    exposure_duration: float | None = None
    detector_gain: str | None = None

    @classmethod
    def create(cls, settings_lines: list[str]) -> InstrumentSettings:
        fluorescence_channel_settings = cls._get_fluorescence_settings(
            settings_lines[0]
        )
        transmitted_light = None
        if not fluorescence_channel_settings:
            transmitted_light = cls._get_transmitted_light_out_of_channel_settings(
                settings_lines[0]
            )
        settings_dict, non_kv_settings = parse_settings(settings_lines[1:])
        if not transmitted_light:
            transmitted_light = cls._get_transmitted_light(non_kv_settings)

        if exposure_duration := settings_dict.get("Integration time"):
            exposure_duration = str(exposure_duration).split()[0]

        return InstrumentSettings(
            auto_focus=cls._get_auto_focus(non_kv_settings),
            detector_distance=cls._get_detector_distance(non_kv_settings),
            fluorescent_tag=fluorescence_channel_settings.get("fluorescent_tag"),
            excitation_wavelength=try_float_or_none(
                fluorescence_channel_settings.get("excitation_wavelength")
            ),
            detector_wavelength=try_float_or_none(
                fluorescence_channel_settings.get("detector_wavelength")
            ),
            transmitted_light=transmitted_light,
            illumination=try_float_or_none(settings_dict.get("LED intensity")),
            exposure_duration=try_float_or_none(exposure_duration),
            detector_gain=settings_dict.get("Camera gain"),
        )

    @classmethod
    def _get_fluorescence_settings(cls, settings_header: str) -> dict[str, str]:
        if matches := re.match(CHANNEL_HEADER_REGEX, settings_header):
            return {key: str(value) for key, value in matches.groupdict().items()}
        return {}

    @classmethod
    def _get_auto_focus(cls, settings: list[str]) -> bool:
        return any(str_ in settings for str_ in AUTOFOCUS_STRINGS)

    @classmethod
    def _get_detector_distance(cls, settings: list[str]) -> float | None:
        if match := re.search(DETECTOR_DISTANCE_REGEX, "\n".join(settings)):
            return try_float(match.groups()[0], "Detector Distance")
        return None

    @classmethod
    def _get_transmitted_light(
        cls, settings: list[str]
    ) -> TransmittedLightSetting | None:
        for line in settings:
            if line in TRANSMITTED_LIGHT_MAP:
                return TRANSMITTED_LIGHT_MAP[line]
        return None

    @classmethod
    def _get_transmitted_light_out_of_channel_settings(
        cls, channel_setting: str
    ) -> TransmittedLightSetting | None:
        keys = "|".join(TRANSMITTED_LIGHT_MAP.keys())
        pattern = rf"\b(?:{keys})\b"
        if match := re.search(pattern, channel_setting):
            return TRANSMITTED_LIGHT_MAP[match.group()]
        return None


@dataclass(frozen=True)
class ReadSection:
    image_mode: DetectionType
    magnification_setting: float | None
    image_count_setting: float | None
    instrument_settings_list: list[InstrumentSettings]

    @classmethod
    def create(cls, reader: LinesReader) -> ReadSection:
        top_read_lines = list(reader.pop_until(SETTINGS_SECTION_REGEX))

        detection_type = cls._get_detection_type("\n".join(top_read_lines))
        instrument_settings_list = cls._get_instrument_settings_list(reader)

        bottom_read_lines = list(reader.pop_until_empty())
        read_settings, _ = parse_settings(top_read_lines + bottom_read_lines)

        if objective := read_settings.get("Objective"):
            objective = str(objective).replace("x", "")

        return ReadSection(
            image_mode=detection_type,
            magnification_setting=try_float_or_none(objective),
            image_count_setting=cls._get_image_count_setting(read_settings),
            instrument_settings_list=instrument_settings_list,
        )

    @classmethod
    def _get_detection_type(cls, read_chunk: str) -> DetectionType:
        if DetectionType.SINGLE_IMAGE.value in read_chunk:
            return DetectionType.SINGLE_IMAGE
        elif DetectionType.MONTAGE.value in read_chunk:
            return DetectionType.MONTAGE
        elif DetectionType.Z_STACK.value in read_chunk:
            return DetectionType.Z_STACK

        msg = f"Measurement mode not found; expected to find one of {sorted(DetectionType._member_names_)}."

        raise AllotropeConversionError(msg)

    @classmethod
    def _get_settings_sections(cls, reader: LinesReader) -> Iterator[list[str]]:
        while True:
            initial_line = reader.get() or ""
            if not re.search(SETTINGS_SECTION_REGEX, initial_line):
                break
            reader.pop()
            lines = [initial_line, *reader.pop_until(r"^\t\w")]
            yield lines

    @classmethod
    def _get_instrument_settings_list(
        cls, reader: LinesReader
    ) -> list[InstrumentSettings]:
        settings_list = []
        auto_focus = False
        for idx, settings_section in enumerate(cls._get_settings_sections(reader)):
            instrument_settings = InstrumentSettings.create(settings_section)
            # The autofocus setting is only reported in the first section but applies to all others
            if idx == 0:
                auto_focus = instrument_settings.auto_focus
            else:
                instrument_settings.auto_focus = auto_focus
            settings_list.append(instrument_settings)
        return settings_list

    @classmethod
    def _get_image_count_setting(cls, read_settings: dict[str, str]) -> float | None:
        montage_rows = read_settings.get("Montage rows")
        montage_columns = read_settings.get("columns")
        if montage_rows and montage_columns:
            return try_float(montage_rows, "Montage rows") * try_float(
                montage_columns, "Montage columns"
            )
        return None


@dataclass(frozen=True)
class ReadData:
    read_sections: list[ReadSection]

    @classmethod
    def create(cls, procedure_details: list[str]) -> ReadData:
        read_type = cls._get_read_type("\n".join(procedure_details))
        if read_type != ReadType.IMAGE:
            raise AllotropeConversionError(UNSUPPORTED_READ_TYPE_ERROR)

        section_lines_reader = SectionLinesReader(procedure_details)

        return ReadData(
            read_sections=[
                ReadSection.create(read_section)
                for read_section in section_lines_reader.iter_sections("^Read\t")
            ]
        )

    @classmethod
    def _get_read_type(cls, procedure_details: str) -> ReadType:
        if ReadType.KINETIC.value in procedure_details:
            return ReadType.KINETIC
        elif ReadType.AREASCAN.value in procedure_details:
            return ReadType.AREASCAN
        elif ReadType.SPECTRAL.value in procedure_details:
            return ReadType.SPECTRAL
        elif ReadType.ENDPOINT.value in procedure_details:
            return ReadType.ENDPOINT
        elif ReadType.IMAGE.value in procedure_details:
            return ReadType.IMAGE

        msg = f"Read type not found; expected to find one of {sorted(ReadType._member_names_)}."
        raise AllotropeConversionError(msg)


def create_results(
    result_lines: list[str] | None,
    header_data: HeaderData,
    read_data: ReadData,
    sample_identifiers: dict[str, str],
) -> list[MeasurementGroup]:
    if not result_lines:
        return [
            MeasurementGroup(
                measurement_time=header_data.datetime,
                plate_well_count=header_data.plate_well_count,
                analytical_method_identifier=header_data.protocol_file_path,
                experimental_data_identifier=header_data.experiment_file_path,
                measurements=[
                    _create_measurement(
                        NOT_APPLICABLE,
                        header_data,
                        read_section,
                        instrument_settings,
                        METADATA_ONLY,
                        None,
                    )
                    for read_section in read_data.read_sections
                    for instrument_settings in read_section.instrument_settings_list
                ],
            )
        ]
    if result_lines[0].strip() != "Results":
        msg = f"Expected the first line of the results section '{result_lines[0]}' to be 'Results'."
        raise AllotropeConversionError(msg)

    # Create dataframe from tabular data and forward fill empty values in index
    data = read_csv(StringIO("\n".join(result_lines[1:])), sep="\t")
    data = data.set_index(data.index.to_series().ffill(axis="index").values)

    image_features = defaultdict(list)

    for row_name, row in data.iterrows():
        feature_name = row.iloc[-1]
        for col_index, value in enumerate(row.iloc[:-1]):
            well_pos = f"{row_name}{col_index + 1}"
            well_value = try_float_or_nan(value)

            image_features[well_pos].append(
                ImageFeature(
                    identifier=random_uuid_str(),
                    feature=feature_name,
                    result=well_value,
                )
            )

    groups = []
    num_measurements = sum(
        len(read_section.instrument_settings_list)
        for read_section in read_data.read_sections
    )
    for well_position in image_features:
        processed_data = ProcessedData(
            identifier=random_uuid_str(), features=image_features[well_position]
        )
        measurements = [
            _create_measurement(
                well_position,
                header_data,
                read_section,
                instrument_settings,
                sample_identifiers.get(well_position),
                processed_data if num_measurements == 1 else None,
            )
            for read_section in read_data.read_sections
            for instrument_settings in read_section.instrument_settings_list
        ]

        groups.append(
            MeasurementGroup(
                measurement_time=header_data.datetime,
                plate_well_count=len(image_features),
                analytical_method_identifier=header_data.protocol_file_path,
                experimental_data_identifier=header_data.experiment_file_path,
                measurements=measurements,
                processed_data=processed_data if num_measurements > 1 else None,
            )
        )

    return groups


def create_metadata(header_data: HeaderData) -> Metadata:
    return Metadata(
        device_identifier=NOT_APPLICABLE,
        model_number=header_data.model_number or NOT_APPLICABLE,
        equipment_serial_number=header_data.equipment_serial_number,
        software_name=DEFAULT_SOFTWARE_NAME,
        software_version=header_data.software_version,
        file_name=header_data.file_name,
        unc_path=header_data.unc_path,
    )


def _create_measurement(
    well_position: str,
    header_data: HeaderData,
    read_section: ReadSection,
    instrument_settings: InstrumentSettings,
    sample_identifier: str | None,
    processed_data: ProcessedData | None,
) -> Measurement:
    return Measurement(
        type_=MeasurementType.OPTICAL_IMAGING,
        device_type=DEVICE_TYPE,
        identifier=random_uuid_str(),
        sample_identifier=sample_identifier
        or f"{header_data.well_plate_identifier} {well_position}",
        location_identifier=well_position,
        well_plate_identifier=header_data.well_plate_identifier,
        detection_type=DETECTION_TYPE,
        detector_wavelength_setting=instrument_settings.detector_wavelength,
        excitation_wavelength_setting=instrument_settings.excitation_wavelength,
        # TODO: this setting won't get reported at the moment since Gen5 only reports it
        # in micrometers and we don't do conversions on the adapters at the moment
        # detector_distance_setting=instrument_settings.detector_distance,
        detector_gain_setting=instrument_settings.detector_gain,
        magnification_setting=read_section.magnification_setting,
        illumination_setting=instrument_settings.illumination,
        illumination_setting_unit=UNITLESS,
        transmitted_light_setting=instrument_settings.transmitted_light,
        auto_focus_setting=instrument_settings.auto_focus,
        image_count_setting=read_section.image_count_setting,
        fluorescent_tag_setting=instrument_settings.fluorescent_tag,
        exposure_duration_setting=instrument_settings.exposure_duration,
        processed_data=processed_data,
    )
