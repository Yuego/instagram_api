from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import Item

__all__ = ['DiscoverChannelsResponse']


class DiscoverChannelsResponseInterface(ApiResponseInterface):
    auto_load_more_enabled: AnyType
    items: [Item]
    more_available: bool
    next_max_id: str


class DiscoverChannelsResponse(ApiResponse, DiscoverChannelsResponseInterface):
    pass
