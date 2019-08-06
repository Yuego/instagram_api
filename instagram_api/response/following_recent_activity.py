from .base_response import Response
from .model import Story

__all__ = ['FollowingRecentActivityResponse']


class FollowingRecentActivityResponse(Response):
    JSON_PROPERTY_MAP = {
        'stories': [Story],
        'next_max_id': str,
        'auto_load_more_enabled': None,
        'megaphone': None,
    }
