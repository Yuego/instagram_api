from .base_response import ApiResponse
from .model import LocationItem

__all__ = ['FBLocationResponse']


class FBLocationResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'has_more': bool,
        'items': [LocationItem],
        'rank_token': str,
    }
