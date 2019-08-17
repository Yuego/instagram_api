from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['CommentFilterSetResponse']


class CommentFilterSetResponseInterface(ApiResponseInterface):
    pass


class CommentFilterSetResponse(ApiResponse, CommentFilterSetResponseInterface):
    pass
