from .base_response import ApiResponse
from .model import MediaInsights

__all__ = ['MediaInsightsResponse']


class MediaInsightsResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'media_organic_insights': MediaInsights,
    }
