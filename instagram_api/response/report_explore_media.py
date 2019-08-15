from .base_response import ApiResponse

__all__ = ['ReportExploreMediaResponse']


class ReportExploreMediaResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'explore_report_status': None,
    }
