from .base_response import ApiResponse
from .model import User

__all__ = ['SuggestedUsersResponse']


class SuggestedUsersResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'users': [User],
        'is_backup': bool,
    }
