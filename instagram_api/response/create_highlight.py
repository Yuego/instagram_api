from .base_response import Response
from .model import Reel

__all__ = ['CreateHighlightResponse']


class CreateHighlightResponse(Response):
    JSON_PROPERTY_MAP = {
        'reel': Reel,
    }
