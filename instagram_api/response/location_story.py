from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import StoryTray

__all__ = ['LocationStoryResponse']


class LocationStoryResponseInterface(ApiResponseInterface):
    story: StoryTray


class LocationStoryResponse(ApiResponse, LocationStoryResponseInterface):
    pass
