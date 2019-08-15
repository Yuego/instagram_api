from .base_response import ApiResponse
from .model import Collection

__all__ = ['EditCollectionResponse']


class EditCollectionResponse(ApiResponse, Collection):
    JSON_PROPERTY_MAP = {

    }
