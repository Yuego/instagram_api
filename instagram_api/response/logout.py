from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['LogoutResponse']


class LogoutResponseInterface(ApiResponseInterface):
    pass


class LogoutResponse(ApiResponse, LogoutResponseInterface):
    pass
