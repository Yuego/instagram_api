from .base_response import Response
from .model import SharedFollower

__all__ = ['SharedFollowersResponse']


class SharedFollowersResponse(Response):
    JSON_PROPERTY_MAP = {
        'users': [SharedFollower],
    }
