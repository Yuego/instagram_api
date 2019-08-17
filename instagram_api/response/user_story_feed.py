from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import Broadcast, PostLiveItem, Reel

__all__ = ['UserStoryFeedResponse']


class UserStoryFeedResponseInterface(ApiResponseInterface):
    broadcast: Broadcast
    reel: Reel
    post_live_item: PostLiveItem


class UserStoryFeedResponse(ApiResponse, UserStoryFeedResponseInterface):
    pass
