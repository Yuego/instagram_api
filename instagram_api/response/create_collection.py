from .base_response import ApiResponse
from .model import Collection

__all__ = ['CreateCollectionResponse']


class CreateCollectionResponse(ApiResponse, Collection):
    JSON_PROPERTY_MAP = {

    }
