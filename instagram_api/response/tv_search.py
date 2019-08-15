from .base_response import ApiResponse
from .model import TvSearchResult

__all__ = ['TvSearchResponse']


class TvSearchResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'results': [TvSearchResult],
        'num_results': int,
        'rank_token': str,
    }
