from .base_response import ApiResponse
from .model import Item

__all__ = ['LikeFeedResponse']


class LikeFeedResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'auto_load_more_enabled': None,
        'items': [Item],
        'more_available': None,
        'patches': None,
        'last_counted_at': None,
        'num_results': int,
        'next_max_id': str,
    }
