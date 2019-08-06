from .base_response import Response
from .model import Item

__all__ = ['LikeFeedResponse']


class LikeFeedResponse(Response):
    JSON_PROPERTY_MAP = {
        'auto_load_more_enabled': None,
        'items': [Item],
        'more_available': None,
        'patches': None,
        'last_counted_at': None,
        'num_results': int,
        'next_max_id': str,
    }
