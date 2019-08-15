from .base_response import ApiResponse
from .model import Item

__all__ = ['DiscoverChannelsResponse']


class DiscoverChannelsResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'auto_load_more_enabled': None,
        'items': [Item],
        'more_available': bool,
        'next_max_id': str,
    }
