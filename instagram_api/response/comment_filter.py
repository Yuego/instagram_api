from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['CommentFilterResponse']


class CommentFilterResponseInterface(ApiResponseInterface):
    config_value: AnyType


class CommentFilterResponse(ApiResponse, CommentFilterResponseInterface):
    pass
