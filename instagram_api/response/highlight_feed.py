from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import Story, StoryTray, StoryTvChannel

__all__ = ['HighlightFeedResponse']


class HighlightFeedResponseInterface(ApiResponseInterface):
    auto_load_more_enabled: bool
    next_max_id: str
    stories: [Story]
    show_empty_state: bool
    tray: [StoryTray]
    tv_channel: StoryTvChannel


class HighlightFeedResponse(ApiResponse, HighlightFeedResponseInterface):
    pass
