from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import User

__all__ = ['BroadcastJoinRequestCountResponse']


class BroadcastJoinRequestCountResponseInterface(ApiResponseInterface):
    fetch_ts: int
    num_total_requests: int
    num_new_requests: int
    users: [User]
    num_unseen_requests: int


class BroadcastJoinRequestCountResponse(ApiResponse, BroadcastJoinRequestCountResponseInterface):
    pass
