from .base_response import ApiResponse
from .model import FeedItem

__all__ = ['ActiveFeedAdsResponse']


class ActiveFeedAdsResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'feed_items': [FeedItem],
        'next_max_id': str,
        'more_available': bool,
    }
