from .base_response import Response
from .model import DirectThread

__all__ = ['DirectThreadResponse']


class DirectThreadResponse(Response):
    JSON_PROPERTY_MAP = {
        'thread': DirectThread,
    }
