from .base_response import Response
from .model import FeedItem

__all__ = ['ActiveFeedAdsResponse']


class ActiveFeedAdsResponse(Response):
    JSON_PROPERTY_MAP = {
        'feed_items': [FeedItem],
        'next_max_id': int,
        'more_available': bool,
    }
