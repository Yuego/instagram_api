from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['CommentLikeUnlikeResponse']


class CommentLikeUnlikeResponseInterface(ApiResponseInterface):
    pass


class CommentLikeUnlikeResponse(ApiResponse, CommentLikeUnlikeResponseInterface):
    pass
