from .base_response import ApiResponse
from .model import CloseFriends

__all__ = ['CloseFriendsResponse']


class CloseFriendsResponse(ApiResponse, CloseFriends):
    JSON_PROPERTY_MAP = {
        'next_max_id': str,
    }
