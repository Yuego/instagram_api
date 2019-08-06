from .base_response import Response
from .model import LocationItem

__all__ = ['FBLocationResponse']


class FBLocationResponse(Response):
    JSON_PROPERTY_MAP = {
        'has_more': bool,
        'items': [LocationItem],
        'rank_token': str,
    }
