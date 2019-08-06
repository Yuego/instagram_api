from .base_response import Response
from .model import User

__all__ = ['BlockedListResponse']


class BlockedListResponse(Response):
    JSON_PROPERTY_MAP = {
        'blocked_list': [User],
        'next_max_id': str,
        'page_size': None,
    }
