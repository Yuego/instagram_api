from .base_response import Response
from .model import Reel

__all__ = ['TagsStoryResponse']


class TagsStoryResponse(Response):
    JSON_PROPERTY_MAP = {
        'story': Reel,
    }
