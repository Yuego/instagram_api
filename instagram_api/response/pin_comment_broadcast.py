from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['PinCommentBroadcastResponse']


class PinCommentBroadcastResponseInterface(ApiResponseInterface):
    comment_id: int


class PinCommentBroadcastResponse(ApiResponse, PinCommentBroadcastResponseInterface):
    pass
