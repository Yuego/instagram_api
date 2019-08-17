from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import DirectThread

__all__ = ['DirectThreadResponse']


class DirectThreadResponseInterface(ApiResponseInterface):
    thread: DirectThread


class DirectThreadResponse(ApiResponse, DirectThreadResponseInterface):
    pass
