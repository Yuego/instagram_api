from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import Suggested

__all__ = ['RecentSearchesResponse']


class RecentSearchesResponseInterface(ApiResponseInterface):
    recent: [Suggested]


class RecentSearchesResponse(ApiResponse, RecentSearchesResponseInterface):
    pass
