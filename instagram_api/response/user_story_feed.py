from .base_response import ApiResponse
from .model import Broadcast, PostLiveItem, Reel

__all__ = ['UserStoryFeedResponse']


class UserStoryFeedResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'broadcast': Broadcast,
        'reel': Reel,
        'post_live_item': PostLiveItem,
    }
