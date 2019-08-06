from .base_response import Response
from .model import Item

__all__ = ['EditMediaResponse']


class EditMediaResponse(Response):
    JSON_PROPERTY_MAP = {
        'media': Item,
    }
