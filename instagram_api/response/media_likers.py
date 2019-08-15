from .base_response import ApiResponse
from .model import User

__all__ = ['User']


class MediaLikersResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'user_count': int,
        'users': [User],
    }
