from .base_response import ApiResponse
from .model import HiddenEntities

__all__ = ['FacebookHiddenEntitiesResponse']


class FacebookHiddenEntitiesResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'recent': HiddenEntities,
    }
