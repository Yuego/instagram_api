from .base_response import Response
from .model import FriendshipStatus

__all__ = ['FriendshipResponse']


class FriendshipResponse(Response):
    JSON_PROPERTY_MAP = {
        'friendship_status': FriendshipStatus,
    }
