from .base_response import Response
from .model import LiveComment
__all__ = ['PostLiveCommentsResponse']


class PostLiveCommentsResponse(Response):
    JSON_PROPERTY_MAP = {
        'starting_offset': None,
        'ending_offset': None,
        'next_fetch_offset': None,
        'comments': [LiveComment],
        'pinned_comments': [LiveComment],
    }
