from .base_response import Response
from .model import DirectSendItemPayload

__all__ = ['DirectSendItemResponse']


class DirectSendItemResponse(Response):
    JSON_PROPERTY_MAP = {
        'action': None,
        'status_code': None,
        'payload': DirectSendItemPayload,
    }
