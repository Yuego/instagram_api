from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import ArchivedStoriesFeedItem

__all__ = ['ArchivedStoriesFeedResponse']


class ArchivedStoriesFeedResponseInterface(ApiResponseInterface):
    items: [ArchivedStoriesFeedItem]
    num_results: int
    more_available: bool
    max_id: int


class ArchivedStoriesFeedResponse(ApiResponse, ArchivedStoriesFeedResponseInterface):
    pass
