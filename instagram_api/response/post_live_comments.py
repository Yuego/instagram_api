from .base_response import ApiResponse
from .model import LiveComment
__all__ = ['PostLiveCommentsResponse']


class PostLiveCommentsResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'starting_offset': None,
        'ending_offset': None,
        'next_fetch_offset': None,
        'comments': [LiveComment],
        'pinned_comments': [LiveComment],
    }
