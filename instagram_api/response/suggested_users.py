from .base_response import Response
from .model import User

__all__ = ['SuggestedUsersResponse']


class SuggestedUsersResponse(Response):
    JSON_PROPERTY_MAP = {
        'users': [User],
        'is_backup': bool,
    }
