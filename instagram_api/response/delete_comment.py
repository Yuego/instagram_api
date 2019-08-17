from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['DeleteCommentResponse']


class DeleteCommentResponseInterface(ApiResponseInterface):
    pass


class DeleteCommentResponse(ApiResponse, DeleteCommentResponseInterface):
    pass
