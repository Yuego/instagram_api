from .base_response import Response
from .model import UserList

__all__ = ['FBSearchResponse']


class FBSearchResponse(Response):
    JSON_PROPERTY_MAP = {
        'has_more': bool,
        'list': [UserList],
        'clear_client_cache': bool,
        'has_more': bool,
        'rank_token': str,
    }
