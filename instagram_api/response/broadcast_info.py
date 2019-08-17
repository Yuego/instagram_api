from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import Broadcast
from .model.broadcast import BroadcastInterface

__all__ = ['BroadcastInfoResponse']


class BroadcastInfoResponseInterface(BroadcastInterface):
    pass


class BroadcastInfoResponse(ApiResponse, BroadcastInfoResponseInterface):
    pass
