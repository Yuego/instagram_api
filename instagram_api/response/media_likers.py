from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import User

__all__ = ['User']


class MediaLikersResponseInterface(ApiResponseInterface):
    user_count: int
    users: [User]


class MediaLikersResponse(ApiResponseInterface):
    pass
