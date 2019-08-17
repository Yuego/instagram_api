from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import MediaInsights

__all__ = ['MediaInsightsResponse']


class MediaInsightsResponseInterface(ApiResponseInterface):
    media_organic_insights: MediaInsights


class MediaInsightsResponse(ApiResponse, MediaInsightsResponseInterface):
    pass
