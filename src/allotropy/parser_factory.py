from datetime import tzinfo
from enum import Enum
from typing import Optional, Union

from allotropy.allotrope.allotrope import AllotropeConversionError
from allotropy.parsers.agilent_gen5.agilent_gen5_parser import AgilentGen5Parser
from allotropy.parsers.appbio_absolute_q.appbio_absolute_q_parser import (
    AppbioAbsoluteQParser,
)
from allotropy.parsers.appbio_quantstudio.appbio_quantstudio_parser import (
    AppBioQuantStudioParser,
)
from allotropy.parsers.beckman_pharmspec.pharmspec_parser import PharmSpecParser
from allotropy.parsers.beckman_vi_cell_blu.vi_cell_blu_parser import ViCellBluParser
from allotropy.parsers.beckman_vi_cell_xr.vi_cell_xr_parser import ViCellXRParser
from allotropy.parsers.example_weyland_yutani.example_weyland_yutani_parser import (
    ExampleWeylandYutaniParser,
)
from allotropy.parsers.moldev_softmax_pro.softmax_pro_parser import SoftmaxproParser
from allotropy.parsers.novabio_flex2.novabio_flex2_parser import NovaBioFlexParser
from allotropy.parsers.perkin_elmer_envision.perkin_elmer_envision_parser import (
    PerkinElmerEnvisionParser,
)
from allotropy.parsers.roche_cedex_bioht.roche_cedex_bioht_parser import (
    RocheCedexBiohtParser,
)
from allotropy.parsers.utils.timestamp_parser import TimestampParser
from allotropy.parsers.vendor_parser import VendorParser


class Vendor(Enum):
    AGILENT_GEN5 = "AGILENT_GEN5"
    APPBIO_QUANTSTUDIO = "APPBIO_QUANTSTUDIO"
    APPBIO_ABSOLUTE_Q = "APPBIO_ABSOLUTE_Q"
    BECKMAN_HIAC = "BECKMAN_HIAC"
    BECKMAN_VI_CELL_BLU = "BECKMAN_VI_CELL_BLU"
    BECKMAN_VI_CELL_XR = "BECKMAN_VI_CELL_XR"
    EXAMPLE_WEYLAND_YUTANI = "EXAMPLE_WEYLAND_YUTANI"
    MOLDEV_SOFTMAX_PRO = "MOLDEV_SOFTMAX_PRO"
    NOVABIO_FLEX2 = "NOVABIO_FLEX2"
    PERKIN_ELMER_ENVISION = "PERKIN_ELMER_ENVISION"
    ROCHE_CEDEX_BIOHT = "ROCHE_CEDEX_BIOHT"


VendorType = Union[Vendor, str]


_VENDOR_TO_PARSER: dict[Vendor, type[VendorParser]] = {
    Vendor.AGILENT_GEN5: AgilentGen5Parser,
    Vendor.APPBIO_QUANTSTUDIO: AppBioQuantStudioParser,
    Vendor.APPBIO_ABSOLUTE_Q: AppbioAbsoluteQParser,
    Vendor.BECKMAN_HIAC: PharmSpecParser,
    Vendor.BECKMAN_VI_CELL_BLU: ViCellBluParser,
    Vendor.BECKMAN_VI_CELL_XR: ViCellXRParser,
    Vendor.EXAMPLE_WEYLAND_YUTANI: ExampleWeylandYutaniParser,
    Vendor.NOVABIO_FLEX2: NovaBioFlexParser,
    Vendor.MOLDEV_SOFTMAX_PRO: SoftmaxproParser,
    Vendor.PERKIN_ELMER_ENVISION: PerkinElmerEnvisionParser,
    Vendor.ROCHE_CEDEX_BIOHT: RocheCedexBiohtParser,
}


class ParserFactory:
    def __init__(self) -> None:
        pass

    def create(
        self, vendor_type: VendorType, default_timezone: Optional[tzinfo] = None
    ) -> VendorParser:
        try:
            timestamp_parser = TimestampParser(default_timezone)
            return _VENDOR_TO_PARSER[Vendor(vendor_type)](timestamp_parser)
        except (ValueError, KeyError) as e:
            error = f"Failed to create parser, unregistered vendor: {vendor_type}"
            raise AllotropeConversionError(error) from e


def get_parser(
    vendor_type: VendorType, default_timezone: Optional[tzinfo] = None
) -> VendorParser:
    return PARSER_FACTORY.create(vendor_type, default_timezone=default_timezone)


PARSER_FACTORY: ParserFactory = ParserFactory()
