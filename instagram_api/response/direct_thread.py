from .base_response import ApiResponse
from .model import DirectThread

__all__ = ['DirectThreadResponse']


class DirectThreadResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'thread': DirectThread,
    }
