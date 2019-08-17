from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import Item

__all__ = ['LikeFeedResponse']


class LikeFeedResponseInterface(ApiResponseInterface):
    auto_load_more_enabled: AnyType
    items: [Item]
    more_available: AnyType
    patches: AnyType
    last_counted_at: AnyType
    num_results: int
    next_max_id: str


class LikeFeedResponse(ApiResponse, LikeFeedResponseInterface):
    pass
