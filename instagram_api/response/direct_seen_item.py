from .base_response import Response
from .model import DirectSeenItemPayload

__all__ = ['DirectSeenItemResponse']


class DirectSeenItemResponse(Response):
    JSON_PROPERTY_MAP = {
        'action': None,
        'payload': DirectSeenItemPayload,
    }
