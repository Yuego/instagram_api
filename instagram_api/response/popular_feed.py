from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import Item

__all__ = ['PopularFeedResponse']


class PopularFeedResponseInterface(ApiResponseInterface):
    next_max_id: str
    more_available: bool
    auto_load_more_enabled: bool
    items: [Item]
    num_results: int
    max_id: int


class PopularFeedResponse(ApiResponse, PopularFeedResponseInterface):
    pass
