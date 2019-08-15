from .base_response import ApiResponse
from .model import Location

__all__ = ['RelatedLocationResponse']


class RelatedLocationResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'related': [Location],
    }
