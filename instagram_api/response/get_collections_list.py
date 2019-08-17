from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import Collection

__all__ = ['GetCollectionsListResponse']


class GetCollectionsListResponseInterface(ApiResponseInterface):
    items: [Collection]
    more_available: bool
    auto_load_more_enabled: bool
    next_max_id: str


class GetCollectionsListResponse(ApiResponse, GetCollectionsListResponseInterface):
    pass
