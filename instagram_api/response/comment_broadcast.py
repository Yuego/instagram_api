from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import Comment

__all__ = ['CommentBroadcastResponse']


class CommentBroadcastResponseInterface(ApiResponseInterface):
    comment: Comment


class CommentBroadcastResponse(ApiResponse, CommentBroadcastResponseInterface):
    pass
