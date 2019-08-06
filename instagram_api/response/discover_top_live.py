from .base_response import Response
from .model import Broadcast, PostLiveItem

__all__ = ['DiscoverTopLiveResponse']


class DiscoverTopLiveResponse(Response):
    JSON_PROPERTY_MAP = {
        'broadcasts': [Broadcast],
        'post_live_broadcasts': [PostLiveItem],
        'score_map': None,
        'more_available': bool,
        'auto_load_more_enabled': bool,
        'next_max_id': str,
    }
