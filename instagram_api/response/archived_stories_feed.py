from .base_response import Response
from .model import ArchivedStoriesFeedItem

__all__ = ['ArchivedStoriesFeedResponse']


class ArchivedStoriesFeedResponse(Response):
    JSON_PROPERTY_MAP = {
        'items': [ArchivedStoriesFeedItem],
        'num_results': int,
        'more_available': bool,
        'max_id': int,
    }
