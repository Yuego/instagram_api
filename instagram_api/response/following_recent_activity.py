from .base_response import ApiResponse
from .model import Story

__all__ = ['FollowingRecentActivityResponse']


class FollowingRecentActivityResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'stories': [Story],
        'next_max_id': str,
        'auto_load_more_enabled': None,
        'megaphone': None,
    }
