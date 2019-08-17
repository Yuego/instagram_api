from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import Insights

__all__ = ['InsightsResponse']


class InsightsResponseInterface(ApiResponseInterface):
    instagram_user: Insights


class InsightsResponse(ApiResponse, InsightsResponseInterface):
    pass
