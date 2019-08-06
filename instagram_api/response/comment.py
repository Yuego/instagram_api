from .base_response import Response
from .model import Comment

__all__ = ['CommentResponse']


class CommentResponse(Response):
    JSON_PROPERTY_MAP = {
        'comment': Comment,
    }
