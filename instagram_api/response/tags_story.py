from .base_response import ApiResponse
from .model import Reel

__all__ = ['TagsStoryResponse']


class TagsStoryResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'story': Reel,
    }
