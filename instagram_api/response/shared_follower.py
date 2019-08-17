from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import SharedFollower

__all__ = ['SharedFollowersResponse']


class SharedFollowersResponseInterface(ApiResponseInterface):
    users: [SharedFollower]


class SharedFollowersResponse(ApiResponse, SharedFollowersResponseInterface):
    pass
