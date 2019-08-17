from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import Item

__all__ = ['UserFeedResponse']


class UserFeedResponseInterface(ApiResponseInterface):
    items: [Item]
    num_results: int
    more_available: bool
    next_max_id: str
    max_id: str
    auto_load_more_enabled: bool


class UserFeedResponse(ApiResponse, UserFeedResponseInterface):
    pass
