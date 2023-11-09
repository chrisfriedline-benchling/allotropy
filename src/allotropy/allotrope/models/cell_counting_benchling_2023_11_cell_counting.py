# generated by datamodel-codegen:
#   filename:  cell-counting.json
#   timestamp: 2023-11-09T15:53:49+00:00

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, Optional, Union

from allotropy.allotrope.models.shared.definitions.custom import (
    TQuantityValueCell,
    TQuantityValueMicroliter,
    TQuantityValueMicrometer,
    TQuantityValueMillionCellsPerMilliliter,
    TQuantityValueMilliSecond,
    TQuantityValueNanometer,
    TQuantityValuePercent,
    TQuantityValueUnitless,
)
from allotropy.allotrope.models.shared.definitions.definitions import (
    TClass,
    TDatacube,
    TDateTimeStampValue,
    TQuantityValue,
    TStringValue,
)


@dataclass
class DiagnosticTraceDocumentItem:
    description: Any


@dataclass
class DiagnosticTraceAggregateDocument:
    diagnostic_trace_document: Optional[list[DiagnosticTraceDocumentItem]] = None


class StatisticalFeature(Enum):
    inner_diameter = "inner diameter"
    plate_heater_temperature = "plate heater temperature"
    linear_velocity = "linear velocity"
    enthalpy_of_fusion = "enthalpy of fusion"
    angular_velocity = "angular velocity"
    purity = "purity"
    intensity = "intensity"
    protein_attenuation_coefficient = "protein attenuation coefficient"
    electron_beam_working_distance = "electron beam working distance"
    temperature = "temperature"
    end_height = "end height"
    relative_humidity = "relative humidity"
    saturation_vapor_pressure = "saturation vapor pressure"
    heat_flow = "heat flow"
    quality_quantification_facet = "quality quantification facet"
    heat_transfer_coefficient = "heat transfer coefficient"
    molar_concentration = "molar concentration"
    average_total_cell_diameter = "average total cell diameter"
    pH = "pH"
    foam_height = "foam height"
    relative_weight_loss_on_drying = "relative weight loss on drying"
    dilution_volume = "dilution volume"
    flow_ratio = "flow ratio"
    electric_conductance = "electric conductance"
    sample_temperature = "sample temperature"
    container_diameter = "container diameter"
    absorbance = "absorbance"
    sample_thickness = "sample thickness"
    humidity = "humidity"
    Raman_intensity = "Raman intensity"
    voltage = "voltage"
    actual_P_P0_result = "actual P/P0 result"
    polyol_reservoir_temperature = "polyol reservoir temperature"
    turbidity = "turbidity"
    enthalpy_of_sublimation = "enthalpy of sublimation"
    osmolality = "osmolality"
    ambient_humidity = "ambient humidity"
    molar_enthalpy_of_vaporization = "molar enthalpy of vaporization"
    total_foam_height = "total foam height"
    strain = "strain"
    thermal_conductivity = "thermal conductivity"
    coating_gap_height = "coating gap height"
    measurement_chamber_free_space_volume = "measurement chamber free space volume"
    fracture_energy = "fracture energy"
    heat_capacity = "heat capacity"
    yield_strain = "yield strain"
    incident_radiation_angle = "incident radiation angle"
    mass_fraction = "mass fraction"
    liquid_height = "liquid height"
    chromatography_column_length = "chromatography column length"
    sample_width = "sample width"
    molar_enthalpy_of_sublimation = "molar enthalpy of sublimation"
    Raman_wavenumber_shift = "Raman wavenumber shift"
    relative_response = "relative response"
    length = "length"
    velocity = "velocity"
    electric_charge = "electric charge"
    molar_mass = "molar mass"
    image_height = "image height"
    concentration = "concentration"
    sample_weight_before_drying = "sample weight before drying"
    dilution_factor = "dilution factor"
    temperature_rate = "temperature rate"
    relative_permittivity = "relative permittivity"
    transition_enthalpy = "transition enthalpy"
    total_gas_flow_rate = "total gas flow rate"
    gloss = "gloss"
    water_mass_fraction = "water mass fraction"
    dielectric_polarization = "dielectric polarization"
    normalized_foam_height = "normalized foam height"
    peak_onset_temperature = "peak onset temperature"
    electric_current = "electric current"
    angle = "angle"
    energy__datum_ = "energy (datum)"
    abrasion_weight = "abrasion weight"
    absolute_water_content = "absolute water content"
    electric_resistance = "electric resistance"
    attenuation_coefficient = "attenuation coefficient"
    molar_enthalpy_of_fusion = "molar enthalpy of fusion"
    water_mass_concentration = "water mass concentration"
    partial_pressure = "partial pressure"
    volume = "volume"
    position_count = "position count"
    thermal_conductance = "thermal conductance"
    dry_sample_weight = "dry sample weight"
    adsorbed_volume_at_STP = "adsorbed volume at STP"
    force = "force"
    birefringence = "birefringence"
    monolayer_quantity = "monolayer quantity"
    peak_temperature = "peak temperature"
    dry_gas_flow_rate = "dry gas flow rate"
    gross_weight = "gross weight"
    sample_weight = "sample weight"
    image_width = "image width"
    m_z = "m/z"
    container_height = "container height"
    flow_rate = "flow rate"
    solvent_reservoir_temperature = "solvent reservoir temperature"
    isocyanate_reservoir_temperature = "isocyanate reservoir temperature"
    ambient_pressure = "ambient pressure"
    eccentricity = "eccentricity"
    mass = "mass"
    molar_absorptivity = "molar absorptivity"
    height = "height"
    column_inner_diameter = "column inner diameter"
    heat_seal_length = "heat seal length"
    specific_surface_area = "specific surface area"
    reference_material_weight = "reference material weight"
    thickness = "thickness"
    tare_weight = "tare weight"
    power = "power"
    chromatography_column_particle_size = "chromatography column particle size"
    saturated_gas_flow_rate = "saturated gas flow rate"
    well_volume = "well volume"
    degassed_sample_weight = "degassed sample weight"
    voltage_range = "voltage range"
    relative_intensity = "relative intensity"
    width = "width"
    yield_stress = "yield stress"
    total_cell_diameter = "total cell diameter"
    stress = "stress"
    relative_pressure__BET_ = "relative pressure (BET)"
    break_stress = "break stress"
    mass_concentration = "mass concentration"
    chromatography_column_film_thickness = "chromatography column film thickness"
    average_particle_size = "average particle size"
    wavelength = "wavelength"
    heat_capacity__dsc_ = "heat capacity (dsc)"
    acquisition_volume = "acquisition volume"
    collision_energy = "collision energy"
    background_corrected_turbidity = "background corrected turbidity"
    mass_change = "mass change"
    chemical_shift = "chemical shift"
    titer = "titer"
    refractive_index = "refractive index"
    enthalpy_of_vaporization = "enthalpy of vaporization"
    volume_fraction = "volume fraction"
    transmittance = "transmittance"
    electric_conductivity = "electric conductivity"
    fill_depth = "fill depth"
    Young_modulus = "Young modulus"
    total_material_height = "total material height"
    specific_rotation = "specific rotation"
    qNMR_purity_result = "qNMR purity result"
    size__datum_ = "size (datum)"
    break_strain = "break strain"
    specific_enthalpy_of_vaporization = "specific enthalpy of vaporization"
    absolute_intensity = "absolute intensity"
    BET_C_constant = "BET C constant"
    plate_well_count = "plate well count"
    plate_temperature = "plate temperature"
    volume_concentration = "volume concentration"
    specific_enthalpy_of_sublimation = "specific enthalpy of sublimation"
    enthalpy = "enthalpy"
    area = "area"
    peak_load_force = "peak load force"
    fluorescence = "fluorescence"
    start_height = "start height"
    polarity = "polarity"
    angle_of_optical_rotation = "angle of optical rotation"
    peak_analyte_amount = "peak analyte amount"
    extrapolated_moisture_content = "extrapolated moisture content"
    inlet_gas_pressure = "inlet gas pressure"
    hardness = "hardness"
    molecular_mass = "molecular mass"
    specific_enthalpy_of_fusion = "specific enthalpy of fusion"
    electric_impedance = "electric impedance"
    hold_up_volume = "hold-up volume"
    particle_size = "particle size"
    diameter = "diameter"
    tablet_thickness = "tablet thickness"
    pressure = "pressure"
    weight_loss = "weight loss"
    cell_path_length = "cell path length"
    glass_transition_temperature = "glass transition temperature"
    specific_heat_capacity = "specific heat capacity"
    wavenumber = "wavenumber"
    reservoir_temperature = "reservoir temperature"
    electric_resistivity = "electric resistivity"
    luminescence = "luminescence"
    compartment_temperature = "compartment temperature"
    viscosity = "viscosity"
    exhaust_gas_flow_rate = "exhaust gas flow rate"
    Raman_interferogram_intensity = "Raman interferogram intensity"
    ambient_temperature = "ambient temperature"
    reflectance = "reflectance"
    detector_view_volume = "detector view volume"
    stirring_rate = "stirring rate"


@dataclass
class StatisticsDocumentItem:
    statistical_feature: StatisticalFeature


@dataclass
class StatisticsAggregateDocument:
    statistics_document: Optional[list[StatisticsDocumentItem]] = None


@dataclass
class Manifest:
    vocabulary: list[str]
    json_schemas: list[str]
    field_id: Optional[str] = None
    field_type: Optional[str] = None
    shapes: Optional[list[str]] = None


@dataclass
class Asm:
    field_asm_manifest: Optional[Union[str, Manifest]] = None


@dataclass
class DataSourceDocumentItem:
    data_source_identifier: TStringValue
    data_source_feature: TStringValue
    field_index: Optional[int] = None


@dataclass
class DataSourceAggregateDocument:
    data_source_document: list[DataSourceDocumentItem]


@dataclass
class SampleDocument:
    sample_identifier: TStringValue
    description: Optional[Any] = None
    batch_identifier: Optional[TStringValue] = None
    sample_role_type: Optional[TClass] = None
    written_name: Optional[TStringValue] = None


@dataclass
class DeviceDocumentItem:
    device_type: TStringValue
    device_identifier: Optional[TStringValue] = None
    model_number: Optional[TStringValue] = None
    product_manufacturer: Optional[TStringValue] = None
    brand_name: Optional[TStringValue] = None
    equipment_serial_number: Optional[TStringValue] = None
    firmware_version: Optional[TStringValue] = None
    field_index: Optional[int] = None


@dataclass
class DeviceSystemDocument:
    asset_management_identifier: Optional[TStringValue] = None
    description: Optional[Any] = None
    brand_name: Optional[TStringValue] = None
    product_manufacturer: Optional[TStringValue] = None
    device_identifier: Optional[TStringValue] = None
    model_number: Optional[TStringValue] = None
    equipment_serial_number: Optional[TStringValue] = None
    firmware_version: Optional[TStringValue] = None
    device_document: Optional[list[DeviceDocumentItem]] = None


@dataclass
class DataSystemDocument:
    data_system_instance_identifier: Optional[TStringValue] = None
    file_name: Optional[TStringValue] = None
    UNC_path: Optional[TStringValue] = None
    software_name: Optional[TStringValue] = None
    software_version: Optional[TStringValue] = None
    ASM_converter_name: Optional[TStringValue] = None
    ASM_converter_version: Optional[TStringValue] = None


@dataclass
class CalculatedDataDocumentItem:
    calculated_data_name: TStringValue
    calculated_result: TQuantityValue
    data_source_aggregate_document: Optional[DataSourceAggregateDocument] = None
    calculated_data_identifier: Optional[TStringValue] = None
    calculation_description: Optional[TStringValue] = None
    field_index: Optional[int] = None


@dataclass
class CalculatedDataAggregateDocument:
    calculated_data_document: list[CalculatedDataDocumentItem]


@dataclass
class ProcessedDataDocumentItem2:
    data_processing_document: Optional[dict[str, Any]] = None
    data_source_aggregate_document: Optional[DataSourceAggregateDocument] = None
    processed_data_identifier: Optional[TStringValue] = None
    field_index: Optional[int] = None


@dataclass
class ProcessedDataAggregateDocument:
    processed_data_document: list[ProcessedDataDocumentItem2]


@dataclass
class DeviceControlDocumentItems:
    device_type: TStringValue
    device_identifier: Optional[TStringValue] = None
    detection_type: Optional[TStringValue] = None
    product_manufacturer: Optional[TStringValue] = None
    brand_name: Optional[TStringValue] = None
    equipment_serial_number: Optional[TStringValue] = None
    model_number: Optional[TStringValue] = None
    firmware_version: Optional[TStringValue] = None
    sample_volume_setting: Optional[TQuantityValueMicroliter] = None
    illumination_setting: Optional[TQuantityValuePercent] = None
    exposure_duration_setting: Optional[TQuantityValueMilliSecond] = None
    detector_gain_setting: Optional[TQuantityValueUnitless] = None
    excitation_wavelength_setting: Optional[TQuantityValueNanometer] = None
    detector_wavelength_setting: Optional[TQuantityValueNanometer] = None


@dataclass
class FluorescenceCellCountingDeviceControlDocumentItem(DeviceControlDocumentItems):
    detector_bandwidth_setting: Optional[TQuantityValueNanometer] = None
    wavelength_filter_cutoff_setting: Optional[TQuantityValueNanometer] = None
    excitation_bandwidth_setting: Optional[TQuantityValueNanometer] = None
    fluorescent_tag_setting: Optional[TStringValue] = None
    field_index: Optional[int] = None


FluorescenceCellCountingDeviceControlDocument = list[
    FluorescenceCellCountingDeviceControlDocumentItem
]


@dataclass
class DataProcessingDocument:
    cell_type_processing_method: Optional[TStringValue] = None
    cell_density_dilution_factor: Optional[TQuantityValueUnitless] = None
    minimum_cell_diameter_setting: Optional[TQuantityValueMicrometer] = None
    maximum_cell_diameter_setting: Optional[TQuantityValueMicrometer] = None


@dataclass
class ProcessedDataDocumentItem1:
    fluorescent_tag_positive_cell_count: TQuantityValueCell
    data_processing_document: Optional[DataProcessingDocument] = None
    data_source_aggregate_document: Optional[DataSourceAggregateDocument] = None
    processed_data_identifier: Optional[TStringValue] = None
    fluorescent_tag_positive_cell_density: Optional[
        TQuantityValueMillionCellsPerMilliliter
    ] = None
    fluorescent_tag_positive_percentage: Optional[TQuantityValuePercent] = None
    field_index: Optional[int] = None


@dataclass
class ProcessedDataAggregateDocument2:
    processed_data_document: list[ProcessedDataDocumentItem1]


@dataclass
class DeviceControlDocumentItem(DeviceControlDocumentItems):
    field_index: Optional[int] = None


@dataclass
class CellCountingDetectorDeviceControlAggregateDocument:
    device_control_document: Optional[list[DeviceControlDocumentItem]] = None


@dataclass
class FluorescenceCellCountingDeviceControlAggregateDocument:
    device_control_document: Optional[
        FluorescenceCellCountingDeviceControlDocument
    ] = None


@dataclass
class FluorescenceCellCountingMeasurementDocumentItems:
    measurement_time: TDateTimeStampValue
    measurement_identifier: TStringValue
    device_control_aggregate_document: FluorescenceCellCountingDeviceControlAggregateDocument
    sample_document: SampleDocument
    processed_data_aggregate_document: ProcessedDataAggregateDocument2
    detection_type: Optional[TStringValue] = None
    calculated_data_aggregate_document: Optional[CalculatedDataAggregateDocument] = None
    statistics_aggregate_document: Optional[StatisticsAggregateDocument] = None


@dataclass
class ProcessedDataDocumentItem:
    viability__cell_counter_: TQuantityValuePercent
    viable_cell_density__cell_counter_: TQuantityValueMillionCellsPerMilliliter
    total_cell_count: TQuantityValueCell
    data_processing_document: Optional[DataProcessingDocument] = None
    data_source_aggregate_document: Optional[DataSourceAggregateDocument] = None
    processed_data_identifier: Optional[TStringValue] = None
    total_cell_density__cell_counter_: Optional[
        TQuantityValueMillionCellsPerMilliliter
    ] = None
    dead_cell_density__cell_counter_: Optional[
        TQuantityValueMillionCellsPerMilliliter
    ] = None
    average_total_cell_diameter: Optional[TQuantityValueMicrometer] = None
    average_live_cell_diameter__cell_counter_: Optional[TQuantityValueMicrometer] = None
    average_dead_cell_diameter__cell_counter_: Optional[TQuantityValueMicrometer] = None
    total_cell_diameter_distribution: Optional[TDatacube] = None
    viable_cell_count: Optional[TQuantityValueCell] = None
    dead_cell_count: Optional[TQuantityValueCell] = None
    average_total_cell_circularity: Optional[TQuantityValueUnitless] = None
    average_viable_cell_circularity: Optional[TQuantityValueUnitless] = None
    field_index: Optional[int] = None


@dataclass
class ProcessedDataAggregateDocument1:
    processed_data_document: list[ProcessedDataDocumentItem]


@dataclass
class CellCountingDetectorMeasurementDocumentItems:
    measurement_time: TDateTimeStampValue
    measurement_identifier: TStringValue
    device_control_aggregate_document: CellCountingDetectorDeviceControlAggregateDocument
    sample_document: SampleDocument
    processed_data_aggregate_document: ProcessedDataAggregateDocument1
    detection_type: Optional[TStringValue] = None
    calculated_data_aggregate_document: Optional[CalculatedDataAggregateDocument] = None
    statistics_aggregate_document: Optional[StatisticsAggregateDocument] = None


@dataclass
class MeasurementAggregateDocument:
    measurement_document: list[
        Union[
            FluorescenceCellCountingMeasurementDocumentItems,
            CellCountingDetectorMeasurementDocumentItems,
        ]
    ]
    diagnostic_trace_aggregate_document: Optional[
        DiagnosticTraceAggregateDocument
    ] = None
    processed_data_aggregate_document: Optional[ProcessedDataAggregateDocument] = None
    calculated_data_aggregate_document: Optional[CalculatedDataAggregateDocument] = None
    statistics_aggregate_document: Optional[StatisticsAggregateDocument] = None


@dataclass
class CellCountingDocumentItem:
    measurement_aggregate_document: MeasurementAggregateDocument
    analyst: Optional[TStringValue] = None
    submitter: Optional[TStringValue] = None


@dataclass
class CellCountingAggregateDocument:
    cell_counting_document: list[CellCountingDocumentItem]
    device_system_document: Optional[DeviceSystemDocument] = None
    data_system_document: Optional[DataSystemDocument] = None
    processed_data_aggregate_document: Optional[ProcessedDataAggregateDocument] = None
    calculated_data_aggregate_document: Optional[CalculatedDataAggregateDocument] = None
    statistics_aggregate_document: Optional[StatisticsAggregateDocument] = None


@dataclass
class Model(Asm):
    field_asm_manifest: Union[str, Manifest]
    cell_counting_aggregate_document: Optional[CellCountingAggregateDocument] = None
