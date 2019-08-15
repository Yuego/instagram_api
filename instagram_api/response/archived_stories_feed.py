from .base_response import ApiResponse
from .model import ArchivedStoriesFeedItem

__all__ = ['ArchivedStoriesFeedResponse']


class ArchivedStoriesFeedResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'items': [ArchivedStoriesFeedItem],
        'num_results': int,
        'more_available': bool,
        'max_id': int,
    }
