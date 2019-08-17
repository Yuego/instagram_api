from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import CountdownSticker

__all__ = ['StoryCountdownsResponse']


class StoryCountdownsResponseInterface(ApiResponseInterface):
    countdowns: [CountdownSticker]


class StoryCountdownsResponse(ApiResponse, StoryCountdownsResponseInterface):
    pass
