from .base_response import ApiResponse
from .model import User

__all__ = ['CommentLikersResponse']


class CommentLikersResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'users': [User],
    }
