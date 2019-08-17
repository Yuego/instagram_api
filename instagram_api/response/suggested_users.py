from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import User

__all__ = ['SuggestedUsersResponse']


class SuggestedUsersResponseInterface(ApiResponseInterface):
    users: [User]
    is_backup: bool


class SuggestedUsersResponse(ApiResponse, SuggestedUsersResponseInterface):
    pass
