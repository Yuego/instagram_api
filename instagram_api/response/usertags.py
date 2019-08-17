from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import Item

__all__ = ['UsertagsResponse']


class UsertagsResponseInterface(ApiResponseInterface):
    num_results: int
    auto_load_more_enabled: AnyType
    items: [Item]
    more_available: AnyType
    next_max_id: str
    total_count: AnyType
    requires_review: AnyType
    new_photos: AnyType


class UsertagsResponse(ApiResponse, UsertagsResponseInterface):
    pass
