from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import FriendshipStatus

__all__ = ['FriendshipResponse']


class FriendshipResponseInterface(ApiResponseInterface):
    friendship_status: FriendshipStatus


class FriendshipResponse(ApiResponse, FriendshipResponseInterface):
    pass
