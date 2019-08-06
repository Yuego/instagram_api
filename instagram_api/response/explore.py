from .base_response import Response
from .model import ExploreItem

__all__ = ['ExploreResponse']


class ExploreResponse(Response):
    JSON_PROPERTY_MAP = {
        'num_results': int,
        'auto_load_more_enabled': None,
        'items': [ExploreItem],
        'more_available': None,
        'next_max_id': str,
        'max_id': str,
        'rank_token': str,
    }
