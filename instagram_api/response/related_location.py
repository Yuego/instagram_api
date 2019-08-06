from .base_response import Response
from .model import Location

__all__ = ['RelatedLocationResponse']


class RelatedLocationResponse(Response):
    JSON_PROPERTY_MAP = {
        'related': [Location],
    }
