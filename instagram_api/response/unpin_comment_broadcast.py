from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['UnpinCommentBroadcastResponse']


class UnpinCommentBroadcastResponseInterface(ApiResponseInterface):
    comment_id: int


class UnpinCommentBroadcastResponse(ApiResponse, UnpinCommentBroadcastResponseInterface):
    pass
