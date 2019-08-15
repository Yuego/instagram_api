from .base_response import ApiResponse
from .model import Insights

__all__ = ['InsightsResponse']


class InsightsResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'instagram_user': Insights,
    }
