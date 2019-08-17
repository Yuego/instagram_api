from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import Suggested

__all__ = ['SuggestedSearchesResponse']


class SuggestedSearchesResponseInterface(ApiResponseInterface):
    suggested: [Suggested]
    rank_token: str


class SuggestedSearchesResponse(ApiResponse, SuggestedSearchesResponseInterface):
    pass
