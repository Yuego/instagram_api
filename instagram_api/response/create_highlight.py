from .base_response import ApiResponse
from .model import Reel

__all__ = ['CreateHighlightResponse']


class CreateHighlightResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'reel': Reel,
    }
