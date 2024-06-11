# generated by datamodel-codegen:
#   filename:  multi-analyte-profiling.schema.json
#   timestamp: 2024-06-04T03:30:34+00:00

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from allotropy.allotrope.models.shared.components.plate_reader import (
    SampleRoleType,
)
from allotropy.allotrope.models.shared.definitions.custom import (
    TQuantityValueMicroliter,
    TQuantityValueNumber,
    TQuantityValueRelativeFluorescenceUnit,
    TQuantityValueUnitless,
)
from allotropy.allotrope.models.shared.definitions.definitions import (
    TDateTimeStampValue,
    TQuantityValue,
    TStringValue,
)


@dataclass(kw_only=True)
class DataSourceDocumentItem:
    data_source_identifier: TStringValue
    data_source_feature: TStringValue
    field_index: int | None = None


@dataclass(kw_only=True)
class DataSourceAggregateDocument:
    data_source_document: list[DataSourceDocumentItem]


@dataclass(kw_only=True)
class Manifest:
    vocabulary: list[str]
    json_schemas: list[str]
    field_id: str | None = None
    field_type: str | None = None
    shapes: list[str] | None = None


@dataclass(kw_only=True)
class DeviceDocumentItem:
    device_identifier: TStringValue | None = None
    device_type: TStringValue | None = None
    model_number: TStringValue | None = None
    product_manufacturer: TStringValue | None = None
    brand_name: TStringValue | None = None
    equipment_serial_number: TStringValue | None = None
    firmware_version: TStringValue | None = None
    field_index: int | None = None


@dataclass(kw_only=True)
class ReferenceMaterialDocument:
    reference_material_identifier: TStringValue | None = None
    batch_identifier: TStringValue | None = None
    expiry_time_prescription: TDateTimeStampValue | None = None


@dataclass(kw_only=True)
class CalibrationResultDocumentItem:
    calibration_result_name: TStringValue | None = None
    calibration_result: TQuantityValueUnitless | None = None


@dataclass(kw_only=True)
class CalibrationResultAggregateDocument:
    calibration_result_document: list[CalibrationResultDocumentItem] | None = None


@dataclass(kw_only=True)
class CalibrationDocumentItem:
    calibration_name: TStringValue | None = None
    calibration_description: TStringValue | None = None
    calibration_time: TDateTimeStampValue | None = None
    expiry_time_prescription: TDateTimeStampValue | None = None
    calibration_report: TStringValue | None = None
    reference_material_document: ReferenceMaterialDocument | None = None
    calibration_result_aggregate_document: CalibrationResultAggregateDocument | None = (
        None
    )


@dataclass(kw_only=True)
class CalibrationAggregateDocument:
    calibration_document: list[CalibrationDocumentItem] | None = None


@dataclass(kw_only=True)
class DeviceSystemDocument:
    asset_management_identifier: TStringValue | None = None
    description: Any | None = None
    brand_name: TStringValue | None = None
    product_manufacturer: TStringValue | None = None
    device_identifier: TStringValue | None = None
    model_number: TStringValue | None = None
    equipment_serial_number: TStringValue | None = None
    firmware_version: TStringValue | None = None
    device_document: list[DeviceDocumentItem] | None = None
    calibration_aggregate_document: CalibrationAggregateDocument | None = None


@dataclass(kw_only=True)
class DataSystemDocument:
    data_system_instance_identifier: TStringValue | None = None
    file_name: TStringValue | None = None
    UNC_path: TStringValue | None = None
    software_name: TStringValue | None = None
    software_version: TStringValue | None = None
    ASM_converter_name: TStringValue | None = None
    ASM_converter_version: TStringValue | None = None


@dataclass(kw_only=True)
class SampleDocument:
    sample_identifier: TStringValue
    description: Any | None = None
    batch_identifier: TStringValue | None = None
    group_identifier: TStringValue | None = None
    sample_role_type: SampleRoleType | None = None
    written_name: TStringValue | None = None
    location_identifier: TStringValue | None = None
    well_plate_identifier: TStringValue | None = None


@dataclass(kw_only=True)
class DeviceControlDocumentItem:
    device_type: TStringValue
    device_identifier: TStringValue | None = None
    model_number: TStringValue | None = None
    product_manufacturer: TStringValue | None = None
    brand_name: TStringValue | None = None
    equipment_serial_number: TStringValue | None = None
    firmware_version: TStringValue | None = None
    sample_volume_setting: TQuantityValueMicroliter | None = None
    dilution_factor_setting: TQuantityValueUnitless | None = None
    detector_gain_setting: TStringValue | None = None
    minimum_assay_bead_count_setting: TQuantityValueNumber | None = None


@dataclass(kw_only=True)
class DeviceControlAggregateDocument:
    device_control_document: list[DeviceControlDocumentItem]


@dataclass(kw_only=True)
class AnalyteDocumentItem:
    analyte_identifier: TStringValue
    analyte_name: TStringValue
    assay_bead_identifier: TStringValue
    assay_bead_count: TQuantityValueNumber
    fluorescence: TQuantityValueRelativeFluorescenceUnit


@dataclass(kw_only=True)
class AnalyteAggregateDocument:
    analyte_document: list[AnalyteDocumentItem]


@dataclass(kw_only=True)
class ErrorDocumentItem:
    error: TStringValue
    error_feature: TStringValue | None = None


@dataclass(kw_only=True)
class ErrorAggregateDocument:
    error_document: list[ErrorDocumentItem] | None = None


@dataclass(kw_only=True)
class MeasurementDocumentItem:
    measurement_identifier: TStringValue
    measurement_time: TDateTimeStampValue
    sample_document: SampleDocument
    device_control_aggregate_document: DeviceControlAggregateDocument
    assay_bead_count: TQuantityValueNumber
    analyte_aggregate_document: AnalyteAggregateDocument
    error_aggregate_document: ErrorAggregateDocument | None = None


@dataclass(kw_only=True)
class MeasurementAggregateDocument:
    measurement_document: list[MeasurementDocumentItem]
    analytical_method_identifier: TStringValue | None = None
    method_version: TStringValue | None = None
    experimental_data_identifier: TStringValue | None = None
    experiment_type: TStringValue | None = None
    container_type: TStringValue | None = None
    plate_well_count: TQuantityValueNumber | None = None


@dataclass(kw_only=True)
class MultiAnalyteProfilingDocumentItem:
    measurement_aggregate_document: MeasurementAggregateDocument
    analyst: TStringValue | None = None
    submitter: TStringValue | None = None


@dataclass(kw_only=True)
class CalculatedDataDocumentItem:
    calculated_data_name: TStringValue
    calculated_result: TQuantityValue
    data_source_aggregate_document: DataSourceAggregateDocument | None = None
    calculated_data_identifier: TStringValue | None = None
    calculation_description: TStringValue | None = None
    field_index: int | None = None


@dataclass(kw_only=True)
class CalculatedDataAggregateDocument:
    calculated_data_document: list[CalculatedDataDocumentItem]


@dataclass(kw_only=True)
class MultiAnalyteProfilingAggregateDocument:
    device_system_document: DeviceSystemDocument
    multi_analyte_profiling_document: list[MultiAnalyteProfilingDocumentItem]
    data_system_document: DataSystemDocument | None = None
    calculated_data_aggregate_document: CalculatedDataAggregateDocument | None = None


@dataclass(kw_only=True)
class Model:
    field_asm_manifest: Manifest | str
    multi_analyte_profiling_aggregate_document: MultiAnalyteProfilingAggregateDocument | None = (
        None
    )