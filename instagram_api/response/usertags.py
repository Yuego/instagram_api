from .base_response import Response
from .model import Item

__all__ = ['UsertagsResponse']


class UsertagsResponse(Response):
    JSON_PROPERTY_MAP = {
        'num_results': int,
        'auto_load_more_enabled': None,
        'items': [Item],
        'more_available': None,
        'next_max_id': str,
        'total_count': None,
        'requires_review': None,
        'new_photos': None,
    }
