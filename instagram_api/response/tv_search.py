from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import TvSearchResult

__all__ = ['TvSearchResponse']


class TvSearchResponseInterface(ApiResponseInterface):
    results: [TvSearchResult]
    num_results: int
    rank_token: str


class TvSearchResponse(ApiResponse, TvSearchResponseInterface):
    pass
