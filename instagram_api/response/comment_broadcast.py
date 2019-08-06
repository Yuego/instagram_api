from .base_response import Response
from .model import Comment

__all__ = ['CommentBroadcastResponse']


class CommentBroadcastResponse(Response):
    JSON_PROPERTY_MAP = {
        'comment': Comment,
    }
