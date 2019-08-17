from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import Hashtag

__all__ = ['HashtagsResponse']


class HashtagsResponseInterface(ApiResponseInterface):
    tags: [Hashtag]


class HashtagsResponse(ApiResponse, HashtagsResponseInterface):
    pass
