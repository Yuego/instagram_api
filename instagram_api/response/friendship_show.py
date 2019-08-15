from .base_response import ApiResponse
from .model import FriendshipStatus

__all__ = ['FriendshipShowResponse']


class FriendshipShowResponse(ApiResponse, FriendshipStatus):
    JSON_PROPERTY_MAP = {

    }
