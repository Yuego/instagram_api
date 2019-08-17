from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import User

__all__ = ['UserInfoResponse']


class UserInfoResponseInterface(ApiResponseInterface):
    megaphone: AnyType
    user: User


class UserInfoResponse(ApiResponse, UserInfoResponseInterface):
    pass
