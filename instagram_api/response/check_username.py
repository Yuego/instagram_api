from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['CheckUsernameResponse']


class CheckUsernameResponseInterface(ApiResponseInterface):
    username: str
    available: AnyType
    error: AnyType
    error_type: AnyType


class CheckUsernameResponse(ApiResponse, CheckUsernameResponseInterface):
    pass
