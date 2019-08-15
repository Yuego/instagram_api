from .base_response import ApiResponse
from .model import Suggested

__all__ = ['SuggestedSearchesResponse']


class SuggestedSearchesResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'suggested': [Suggested],
        'rank_token': str,
    }
