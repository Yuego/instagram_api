from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import Broadcast

__all__ = ['SuggestedBroadcastsResponse']


class SuggestedBroadcastsResponseInterface(ApiResponseInterface):
    broadcasts: [Broadcast]


class SuggestedBroadcastsResponse(ApiResponse, SuggestedBroadcastsResponseInterface):
    pass
