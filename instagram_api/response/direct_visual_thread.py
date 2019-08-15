from .base_response import ApiResponse
from .model import DirectThread

__all__ = ['DirectVisualThreadResponse']


class DirectVisualThreadResponse(ApiResponse, DirectThread):
    JSON_PROPERTY_MAP = {

    }
