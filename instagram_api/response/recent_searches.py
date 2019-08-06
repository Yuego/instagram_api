from .base_response import Response
from .model import Suggested

__all__ = ['RecentSearchesResponse']


class RecentSearchesResponse(Response):
    JSON_PROPERTY_MAP = {
        'recent': [Suggested],
    }
