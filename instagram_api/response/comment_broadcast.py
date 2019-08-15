from .base_response import ApiResponse
from .model import Comment

__all__ = ['CommentBroadcastResponse']


class CommentBroadcastResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'comment': Comment,
    }
