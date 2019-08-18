from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import SavedFeedItem

__all__ = ['CollectionFeedResponse']


class CollectionFeedResponseInterface(ApiResponseInterface):
    collection_id: str
    collection_name: str
    items: [SavedFeedItem]
    num_results: int
    more_available: bool
    auto_load_more_enabled: bool
    next_max_id: str
    has_related_media: bool


class CollectionFeedResponse(ApiResponse, CollectionFeedResponseInterface):
    pass
