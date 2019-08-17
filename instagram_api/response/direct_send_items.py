from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import DirectSendItemPayload

__all__ = ['DirectSendItemsResponse']


class DirectSendItemsResponseInterface(ApiResponseInterface):
    action: AnyType
    status_code: AnyType
    payload: [DirectSendItemPayload]


class DirectSendItemsResponse(ApiResponse, DirectSendItemsResponseInterface):
    pass
