from .base_response import ApiResponse
from .model import SavedFeedItem

__all__ = ['CollectionFeedResponse']


class CollectionFeedResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'collection_id': str,
        'collection_name': str,
        'items': [SavedFeedItem],
        'num_results': int,
        'more_available': bool,
        'auto_load_more_enabled': bool,
        'next_max_id': str,
        'has_related_media': bool,
    }
