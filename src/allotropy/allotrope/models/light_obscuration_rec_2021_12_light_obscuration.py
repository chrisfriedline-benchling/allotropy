# generated by datamodel-codegen:
#   filename:  light-obscuration.json
#   timestamp: 2023-12-04T16:36:57+00:00

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

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
class DistributionItem:
    particle_size: TQuantityValueMicrometer
    cumulative_count: TQuantityValueUnitless
    cumulative_particle_density: TQuantityValueCountsPerMilliliter
    differential_particle_density: TQuantityValueCountsPerMilliliter
    differential_count: TQuantityValueUnitless


@dataclass
class DistributionDocumentItem:
    distribution: Optional[list[DistributionItem]] = None
    data_processing_omission_setting: Optional[TBooleanValue] = None
    field_index: Optional[int] = None


@dataclass
class MeasurementDocument:
    distribution_document: Optional[list[DistributionDocumentItem]] = None


@dataclass
class Model:
    detector_view_volume: TQuantityValueMilliliter
    flush_volume_setting: TQuantityValueMilliliter
    analyst: TStringValue
    dilution_factor_setting: TQuantityValueUnitless
    repetition_setting: TIntValue
    sample_volume_setting: TQuantityValueMilliliter
    detector_identifier: TStringValue
    sample_identifier: TStringValue
    detector_model_number: TStringValue
    measurement_time: TDateTimeValue
    measurement_document: Optional[MeasurementDocument] = None
    measurement_identifier: Optional[TStringValue] = None
    equipment_serial_number: Optional[TStringValue] = None
    model_number: Optional[TStringValue] = None
    manifest: str = "http://purl.allotrope.org/manifests/light-obscuration/REC/2021/12/light-obscuration.manifest"
