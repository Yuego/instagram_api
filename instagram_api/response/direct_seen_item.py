from .base_response import ApiResponse
from .model import DirectSeenItemPayload

__all__ = ['DirectSeenItemResponse']


class DirectSeenItemResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'action': None,
        'payload': DirectSeenItemPayload,
    }
