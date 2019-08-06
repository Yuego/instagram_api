from .base_response import Response
from .model import Suggested

__all__ = ['SuggestedSearchesResponse']


class SuggestedSearchesResponse(Response):
    JSON_PROPERTY_MAP = {
        'suggested': [Suggested],
        'rank_token': str,
    }
