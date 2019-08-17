from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import BroadcastStatusItem

__all__ = ['TopLiveStatusResponse']


class TopLiveStatusResponseInterface(ApiResponseInterface):
    broadcast_status_items: [BroadcastStatusItem]


class TopLiveStatusResponse(ApiResponse, TopLiveStatusResponseInterface):
    pass
