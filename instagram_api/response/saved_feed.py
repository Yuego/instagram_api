from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import SavedFeedItem

__all__ = ['SavedFeedResponse']


class SavedFeedResponseInterface(ApiResponseInterface):
    items: [SavedFeedItem]
    more_available: bool
    next_max_id: str
    auto_load_more_enabled: bool
    num_results: int


class SavedFeedResponse(ApiResponse, SavedFeedResponseInterface):
    pass
