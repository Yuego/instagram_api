from .base_response import Response
from .model import User

__all__ = ['CommentLikersResponse']


class CommentLikersResponse(Response):
    JSON_PROPERTY_MAP = {
        'users': [User],
    }
