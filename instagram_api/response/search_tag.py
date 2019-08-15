from .base_response import ApiResponse
from .model import Tag

__all__ = ['SearchTagResponse']


class SearchTagResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'has_more': bool,
        'results': [Tag],
        'rank_token': str,
    }
