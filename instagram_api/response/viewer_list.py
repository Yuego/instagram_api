from .base_response import ApiResponse
from .model import User

__all__ = ['ViewerListResponse']


class ViewerListResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'users': [User],
    }
