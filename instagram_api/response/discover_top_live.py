from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import Broadcast, PostLiveItem

__all__ = ['DiscoverTopLiveResponse']


class DiscoverTopLiveResponseInterface(ApiResponseInterface):
    broadcasts: [Broadcast]
    post_live_broadcasts: [PostLiveItem]
    score_map: AnyType
    more_available: bool
    auto_load_more_enabled: bool
    next_max_id: str


class DiscoverTopLiveResponse(ApiResponse, DiscoverTopLiveResponseInterface):
    pass
