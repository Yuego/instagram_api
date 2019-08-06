from .base_response import Response
from .model import CloseFriends

__all__ = ['CloseFriendsResponse']


class CloseFriendsResponse(Response, CloseFriends):
    JSON_PROPERTY_MAP = {
        'next_max_id': str,
    }
