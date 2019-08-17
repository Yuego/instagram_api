from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['PushRegisterResponse']


class PushRegisterResponseInterface(ApiResponseInterface):
    pass


class PushRegisterResponse(ApiResponse, PushRegisterResponseInterface):
    pass
