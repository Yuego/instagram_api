from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['CommentCategoryFilterResponse']


class CommentCategoryFilterResponseInterface(ApiResponseInterface):
    disabled: AnyType


class CommentCategoryFilterResponse(ApiResponse, CommentCategoryFilterResponseInterface):
    pass
