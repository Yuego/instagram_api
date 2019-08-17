from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import Reel

__all__ = ['TagsStoryResponse']


class TagsStoryResponseInterface(ApiResponseInterface):
    story: Reel


class TagsStoryResponse(ApiResponse, TagsStoryResponseInterface):
    pass
