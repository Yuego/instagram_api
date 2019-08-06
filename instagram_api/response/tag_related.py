from .base_response import Response
from .model import Related

__all__ = ['TagRelatedResponse']


class TagRelatedResponse(Response):
    JSON_PROPERTY_MAP = {
        'related': [Related],
    }
