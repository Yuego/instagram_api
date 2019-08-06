from .base_response import Response
from .model import Item

__all__ = ['DiscoverChannelsResponse']


class DiscoverChannelsResponse(Response):
    JSON_PROPERTY_MAP = {
        'auto_load_more_enabled': None,
        'items': [Item],
        'more_available': bool,
        'next_max_id': str,
    }
