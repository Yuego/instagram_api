from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import ExploreItem

__all__ = ['ExploreResponse']


class ExploreResponseInterface(ApiResponseInterface):
    num_results: int
    auto_load_more_enabled: AnyType
    items: [ExploreItem]
    more_available: AnyType
    next_max_id: str
    max_id: str
    rank_token: str


class ExploreResponse(ApiResponse, ExploreResponseInterface):
    pass
