from .base_response import Response
from .model import Item

__all__ = ['MediaInfoResponse']


class MediaInfoResponse(Response):
    JSON_PROPERTY_MAP = {
        'auto_load_more_enabled': None,
        'num_results': int,
        'more_available': bool,
        'items': [Item],
    }
