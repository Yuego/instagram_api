from .base_response import ApiResponse
from .model import User

__all__ = ['CreateBusinessInfoResponse']


class CreateBusinessInfoResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'users': [User],
    }
