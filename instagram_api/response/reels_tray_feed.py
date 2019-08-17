from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import Broadcast, PostLive, StoryTray, TraySuggestions

__all__ = ['ReelsTrayFeedResponse']


class ReelsTrayFeedResponseInterface(ApiResponseInterface):
    story_ranking_token: str
    broadcasts: [Broadcast]
    tray: [StoryTray]
    post_live: PostLive
    sticker_version: int
    face_filter_nux_version: int
    stories_viewer_gestures_nux_eligible: bool
    has_new_nux_story: bool
    suggestions: [TraySuggestions]


class ReelsTrayFeedResponse(ApiResponse, ReelsTrayFeedResponseInterface):
    pass
