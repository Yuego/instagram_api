from .base_response import Response
from .model import Location

__all__ = ['LocationResponse']


class LocationResponse(Response):
    JSON_PROPERTY_MAP = {
        'venues': [Location],
        'request_id': str,
    }
