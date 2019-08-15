from .base_response import ApiResponse
from .model import Related

__all__ = ['TagRelatedResponse']


class TagRelatedResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'related': [Related],
    }
