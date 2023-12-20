# generated by datamodel-codegen:
#   filename:  light-obscuration.json
#   timestamp: 2023-12-20T17:41:00+00:00

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Union

from allotropy.allotrope.models.shared.definitions.custom import (
    TQuantityValueCountsPerMilliliter,
    TQuantityValueMicrometer,
    TQuantityValueMilliliter,
    TQuantityValueUnitless,
)
from allotropy.allotrope.models.shared.definitions.definitions import (
    TBooleanValue,
    TDateTimeValue,
    TIntValue,
    TStringValue,
)


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


@dataclass
class TDataSourceAggregateDocument:
    data_source_document: list[DataSourceDocumentItem]


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
class DistributionItem:
    particle_size: TQuantityValueMicrometer
    cumulative_count: TQuantityValueUnitless
    cumulative_particle_density: TQuantityValueCountsPerMilliliter
    differential_particle_density: Optional[TQuantityValueCountsPerMilliliter] = None
    differential_count: Optional[TQuantityValueUnitless] = None


@dataclass
class DistributionDocumentItem:
    distribution: Optional[list[DistributionItem]] = None
    data_processing_omission_setting: Optional[TBooleanValue] = None
    field_index: Optional[int] = None


@dataclass
class MeasurementDocumentItem:
    measurement_identifier: TStringValue
    distribution_document: list[DistributionDocumentItem]


@dataclass
class MeasurementAggregateDocument:
    measurement_document: Optional[list[MeasurementDocumentItem]] = None


@dataclass
class LightObscurationDocumentItem:
    measurement_aggregate_document: MeasurementAggregateDocument
    detector_view_volume: TQuantityValueMilliliter
    flush_volume_setting: TQuantityValueMilliliter
    dilution_factor_setting: TQuantityValueUnitless
    repetition_setting: TIntValue
    sample_volume_setting: TQuantityValueMilliliter
    detector_identifier: TStringValue
    sample_identifier: TStringValue
    detector_model_number: TStringValue
    measurement_time: TDateTimeValue
    analyst: TStringValue
    equipment_serial_number: Optional[TStringValue] = None
    model_number: Optional[TStringValue] = None
    submitter: Optional[TStringValue] = None


@dataclass
class LightObscurationAggregateDocument:
    light_obscuration_document: list[LightObscurationDocumentItem]
    calculated_data_aggregate_document: Optional[
        TCalculatedDataAggregateDocument
    ] = None


@dataclass
class Model(Asm):
    field_asm_manifest: Union[str, Manifest]
    light_obscuration_aggregate_document: Optional[
        LightObscurationAggregateDocument
    ] = None