from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import DirectSeenItemPayload

__all__ = ['DirectSeenItemResponse']


class DirectSeenItemResponseInterface(ApiResponseInterface):
    action: AnyType
    payload: DirectSeenItemPayload


class DirectSeenItemResponse(ApiResponse, DirectSeenItemResponseInterface):
    pass
