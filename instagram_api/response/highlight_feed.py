from .base_response import Response
from .model import Story, StoryTray, StoryTvChannel

__all__ = ['HighlightFeedResponse']


class HighlightFeedResponse(Response):
    JSON_PROPERTY_MAP = {
        'auto_load_more_enabled': bool,
        'next_max_id': str,
        'stories': [Story],
        'show_empty_state': bool,
        'tray': [StoryTray],
        'tv_channel': StoryTvChannel,
    }