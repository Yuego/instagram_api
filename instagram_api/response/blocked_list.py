from .base_response import ApiResponse
from .model import User

__all__ = ['BlockedListResponse']


class BlockedListResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'blocked_list': [User],
        'next_max_id': str,
        'page_size': None,
    }
