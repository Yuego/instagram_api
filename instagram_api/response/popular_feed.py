from .base_response import Response
from .model import Item

__all__ = ['PopularFeedResponse']


class PopularFeedResponse(Response):
    JSON_PROPERTY_MAP = {
        'next_max_id': str,
        'more_available': bool,
        'auto_load_more_enabled': bool,
        'items': [Item],
        'num_results': int,
        'max_id': int,
    }
