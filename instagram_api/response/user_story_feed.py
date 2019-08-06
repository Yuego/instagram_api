from .base_response import Response
from .model import Broadcast, PostLiveItem, Reel

__all__ = ['UserStoryFeedResponse']


class UserStoryFeedResponse(Response):
    JSON_PROPERTY_MAP = {
        'broadcast': Broadcast,
        'reel': Reel,
        'post_live_item': PostLiveItem,
    }
