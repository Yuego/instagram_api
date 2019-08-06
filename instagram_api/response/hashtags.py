from .base_response import Response
from .model import Hashtag

__all__ = ['HashtagsResponse']


class HashtagsResponse(Response):
    JSON_PROPERTY_MAP = {
        'tags': [Hashtag],
    }
