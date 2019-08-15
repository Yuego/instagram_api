from .base_response import ApiResponse
from .model import Item

__all__ = ['EditMediaResponse']


class EditMediaResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'media': Item,
    }
