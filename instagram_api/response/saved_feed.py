from .base_response import ApiResponse
from .model import SavedFeedItem

__all__ = ['SavedFeedResponse']


class SavedFeedResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'items': [SavedFeedItem],
        'more_available': bool,
        'next_max_id': str,
        'auto_load_more_enabled': bool,
        'num_results': int,
    }
