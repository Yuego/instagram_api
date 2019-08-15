from .base_response import ApiResponse
from .model import Broadcast, PostLive, StoryTray, TraySuggestions

__all__ = ['ReelsTrayFeedResponse']


class ReelsTrayFeedResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'story_ranking_token': str,
        'broadcasts': [Broadcast],
        'tray': [StoryTray],
        'post_live': PostLive,
        'sticker_version': int,
        'face_filter_nux_version': int,
        'stories_viewer_gestures_nux_eligible': bool,
        'has_new_nux_story': bool,
        'suggestions': [TraySuggestions],
    }
