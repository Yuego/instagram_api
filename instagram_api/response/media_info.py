from .base_response import ApiResponse
from .model import Item

__all__ = ['MediaInfoResponse']


class MediaInfoResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'auto_load_more_enabled': None,
        'num_results': int,
        'more_available': bool,
        'items': [Item],
    }
