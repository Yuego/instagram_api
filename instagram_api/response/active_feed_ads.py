from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import FeedItem

__all__ = ['ActiveFeedAdsResponse']


class ActiveFeedAdsResponseInterface(ApiResponseInterface):
    feed_items: [FeedItem]
    next_max_id: str
    more_available: bool


class ActiveFeedAdsResponse(ApiResponse, ActiveFeedAdsResponseInterface):
    pass
