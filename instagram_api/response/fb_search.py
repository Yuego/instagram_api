from .base_response import ApiResponse
from .model import UserList

__all__ = ['FBSearchResponse']


class FBSearchResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'has_more': bool,
        'list': [UserList],
        'clear_client_cache': bool,
        'has_more': bool,
        'rank_token': str,
    }
