from .base_response import ApiResponse
from .model import Item

__all__ = ['UserFeedResponse']


class UserFeedResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'items': [Item],
        'num_results': int,
        'more_available': bool,
        'next_max_id': str,
        'max_id': str,
        'auto_load_more_enabled': bool,
    }
