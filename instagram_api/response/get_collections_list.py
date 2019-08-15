from .base_response import ApiResponse
from .model import Collection

__all__ = ['GetCollectionsListResponse']


class GetCollectionsListResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'items': [Collection],
        'more_available': bool,
        'auto_load_more_enabled': bool,
        'next_max_id': str,
    }
