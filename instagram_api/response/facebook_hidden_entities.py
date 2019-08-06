from .base_response import Response
from .model import HiddenEntities

__all__ = ['FacebookHiddenEntitiesResponse']


class FacebookHiddenEntitiesResponse(Response):
    JSON_PROPERTY_MAP = {
        'recent': HiddenEntities,
    }
