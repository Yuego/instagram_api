from .base_response import Response
from .model import FriendshipStatus

__all__ = ['FriendshipShowResponse']


class FriendshipShowResponse(Response, FriendshipStatus):
    JSON_PROPERTY_MAP = {

    }
