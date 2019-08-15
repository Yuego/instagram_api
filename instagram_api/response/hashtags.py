from .base_response import ApiResponse
from .model import Hashtag

__all__ = ['HashtagsResponse']


class HashtagsResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'tags': [Hashtag],
    }
