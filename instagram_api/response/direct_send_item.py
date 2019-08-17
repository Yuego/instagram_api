from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import DirectSendItemPayload

__all__ = ['DirectSendItemResponse']


class DirectSendItemResponseInterface(ApiResponseInterface):
    action: AnyType
    status_code: AnyType
    payload: DirectSendItemPayload


class DirectSendItemResponse(ApiResponse, DirectSendItemResponseInterface):
    pass
