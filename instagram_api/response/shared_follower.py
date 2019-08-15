from .base_response import ApiResponse
from .model import SharedFollower

__all__ = ['SharedFollowersResponse']


class SharedFollowersResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'users': [SharedFollower],
    }
