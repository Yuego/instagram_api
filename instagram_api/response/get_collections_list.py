from .base_response import Response
from .model import Collection

__all__ = ['GetCollectionsListResponse']


class GetCollectionsListResponse(Response):
    JSON_PROPERTY_MAP = {
        'items': [Collection],
        'more_available': bool,
        'auto_load_more_enabled': bool,
        'next_max_id': str,
    }
