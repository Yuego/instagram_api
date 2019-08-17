from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import UserList

__all__ = ['FBSearchResponse']


class FBSearchResponseInterface(ApiResponseInterface):
    has_more: bool
    list: [UserList]
    clear_client_cache: bool
    rank_token: str


class FBSearchResponse(ApiResponse, FBSearchResponseInterface):
    pass
