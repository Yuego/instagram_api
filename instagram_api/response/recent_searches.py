from .base_response import ApiResponse
from .model import Suggested

__all__ = ['RecentSearchesResponse']


class RecentSearchesResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'recent': [Suggested],
    }
