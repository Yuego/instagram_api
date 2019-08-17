from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import Comment

__all__ = ['CommentResponse']


class CommentResponseInterface(ApiResponseInterface):
    comment: Comment


class CommentResponse(ApiResponse, CommentResponseInterface):
    pass
