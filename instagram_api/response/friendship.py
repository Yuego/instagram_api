from .base_response import ApiResponse
from .model import FriendshipStatus

__all__ = ['FriendshipResponse']


class FriendshipResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'friendship_status': FriendshipStatus,
    }
