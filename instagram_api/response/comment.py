from .base_response import ApiResponse
from .model import Comment

__all__ = ['CommentResponse']


class CommentResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'comment': Comment,
    }
