from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['ReportExploreMediaResponse']


class ReportExploreMediaResponseInterface(ApiResponseInterface):
    explore_report_status: AnyType


class ReportExploreMediaResponse(ApiResponse, ReportExploreMediaResponseInterface):
    pass
