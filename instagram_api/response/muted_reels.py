from .base_response import Response
from .model import User

__all__ = ['MutedReelsResponse']


class MutedReelsResponse(Response):
    JSON_PROPERTY_MAP = {
        'users': [User],
        'next_max_id': str,
        'page_size': None,
        'big_list': None,
    }
