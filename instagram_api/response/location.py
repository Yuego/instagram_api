from .base_response import ApiResponse
from .model import Location

__all__ = ['LocationResponse']


class LocationResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'venues': [Location],
        'request_id': str,
    }
