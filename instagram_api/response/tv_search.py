from .base_response import Response
from .model import TvSearchResult

__all__ = ['TvSearchResponse']


class TvSearchResponse(Response):
    JSON_PROPERTY_MAP = {
        'results': [TvSearchResult],
        'num_results': int,
        'rank_token': str,
    }
