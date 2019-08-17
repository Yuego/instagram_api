from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['BroadcastLikeResponse']


class BroadcastLikeResponseInterface(ApiResponseInterface):
    likes: AnyType


class BroadcastLikeResponse(ApiResponse, BroadcastLikeResponseInterface):
    pass
