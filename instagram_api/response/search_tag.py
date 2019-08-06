from .base_response import Response
from .model import Tag

__all__ = ['SearchTagResponse']


class SearchTagResponse(Response):
    JSON_PROPERTY_MAP = {
        'has_more': bool,
        'results': [Tag],
        'rank_token': str,
    }
