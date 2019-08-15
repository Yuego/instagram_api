from .base_response import ApiResponse
from .model import DirectSendItemPayload

__all__ = ['DirectSendItemResponse']


class DirectSendItemResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'action': None,
        'status_code': None,
        'payload': DirectSendItemPayload,
    }
