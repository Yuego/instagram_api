from .base_response import Response
from .model import User

__all__ = ['User']


class MediaLikersResponse(Response):
    JSON_PROPERTY_MAP = {
        'user_count': int,
        'users': [User],
    }
