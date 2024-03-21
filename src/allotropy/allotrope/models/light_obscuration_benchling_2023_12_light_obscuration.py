# generated by datamodel-codegen:
#   filename:  light-obscuration.json
#   timestamp: 2024-03-21T18:00:57+00:00

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional, Union

from allotropy.allotrope.models.shared.definitions.custom import (
    TQuantityValueCountsPerMilliliter,
    TQuantityValueMicrometer,
    TQuantityValueMilliliter,
    TQuantityValueUnitless,
)
from allotropy.allotrope.models.shared.definitions.definitions import (
    TBooleanValue,
    TDateTimeStampValue,
    TIntValue,
    TStringValue,
)


@dataclass
class DataSourceDocumentItem:
    data_source_identifier: TStringValue
    data_source_feature: TStringValue


@dataclass
class TDataSourceAggregateDocument:
    data_source_document: list[DataSourceDocumentItem]


@dataclass
class SampleDocument:
    sample_identifier: TStringValue


@dataclass
class Manifest:
    vocabulary: list[str]
    json_schemas: list[str]
    field_id: Optional[str] = None
    field_type: Optional[str] = None
    shapes: Optional[list[str]] = None


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
class DeviceDocumentItem:
    detector_identifier: TStringValue
    dectector_model_number: Optional[TStringValue] = None
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
class CalculatedDataDocumentItem:
    calculated_data_name: TStringValue
    calculated_result: Union[
        TQuantityValueMicrometer,
        TQuantityValueUnitless,
        TQuantityValueCountsPerMilliliter,
    ]
    data_source_aggregate_document: Optional[TDataSourceAggregateDocument] = None
    calculated_data_identifier: Optional[TStringValue] = None
    calculation_description: Optional[TStringValue] = None


@dataclass
class TCalculatedDataAggregateDocument:
    calculated_data_document: list[CalculatedDataDocumentItem]


@dataclass
class DeviceControlDocumentItem:
    flush_volume_setting: TQuantityValueMilliliter
    detector_view_volume: TQuantityValueMilliliter
    repetition_setting: TIntValue
    sample_volume_setting: TQuantityValueMilliliter


@dataclass
class DataProcessingDocument:
    dilution_factor_setting: Optional[TQuantityValueUnitless] = None
    data_processing_omission_setting: Optional[TBooleanValue] = None


@dataclass
class DistributionItem:
    particle_size: TQuantityValueMicrometer
    cumulative_count: TQuantityValueUnitless
    cumulative_particle_density: TQuantityValueCountsPerMilliliter
    distribution_identifier: Optional[TStringValue] = None
    differential_particle_density: Optional[TQuantityValueCountsPerMilliliter] = None
    differential_count: Optional[TQuantityValueUnitless] = None


@dataclass
class DistributionDocumentItem:
    distribution: Optional[list[DistributionItem]] = None
    field_index: Optional[int] = None


@dataclass
class DistributionAggregateDocument:
    distribution_document: list[DistributionDocumentItem]


@dataclass
class Asm:
    field_asm_manifest: Optional[Union[str, Manifest]] = None


@dataclass
class DeviceControlDocumentItemModel(DeviceControlDocumentItem):
    field_index: Optional[int] = None


@dataclass
class DeviceControlAggregateDocument:
    device_control_document: Optional[list[DeviceControlDocumentItemModel]] = None


@dataclass
class ProcessedDataDocumentItem:
    data_processing_document: Optional[DataProcessingDocument] = None
    distribution_aggregate_document: Optional[DistributionAggregateDocument] = None
    field_index: Optional[int] = None


@dataclass
class ProcessedDataAggregateDocument:
    processed_data_document: list[ProcessedDataDocumentItem]


@dataclass
class MeasurementDocumentItem:
    measurement_identifier: TStringValue
    measurement_time: TDateTimeStampValue
    device_control_aggregate_document: Optional[DeviceControlAggregateDocument] = None
    sample_document: Optional[SampleDocument] = None
    processed_data_aggregate_document: Optional[ProcessedDataAggregateDocument] = None


@dataclass
class MeasurementAggregateDocument:
    analyst: TStringValue
    submitter: Optional[TStringValue] = None
    measurement_document: Optional[list[MeasurementDocumentItem]] = None


@dataclass
class LightObscurationDocumentItem:
    measurement_aggregate_document: MeasurementAggregateDocument


@dataclass
class LightObscurationAggregateDocument:
    light_obscuration_document: list[LightObscurationDocumentItem]
    data_system_document: Optional[DataSystemDocument] = None
    device_system_document: Optional[DeviceSystemDocument] = None
    calculated_data_aggregate_document: Optional[
        TCalculatedDataAggregateDocument
    ] = None


@dataclass
class Model(Asm):
    field_asm_manifest: Union[str, Manifest]
    light_obscuration_aggregate_document: Optional[
        LightObscurationAggregateDocument
    ] = None
