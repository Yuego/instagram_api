from .base_response import Response
from .model import MediaInsights

__all__ = ['MediaInsightsResponse']


class MediaInsightsResponse(Response):
    JSON_PROPERTY_MAP = {
        'media_organic_insights': MediaInsights,
    }
