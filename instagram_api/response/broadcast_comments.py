from .base_response import ApiResponse
from .model import Comment

__all__ = ['BroadcastCommentsResponse']


class BroadcastCommentsResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'comments': [Comment],
        'comment_count': int,
        'live_seconds_per_comment': int,
        'has_more_headload_comments': bool,
        'is_first_fetch': str,
        'comment_likes_enabled': bool,
        'pinned_comment': Comment,
        'system_comments': [Comment],
        'has_more_comments': bool,
        'caption_is_edited': bool,
        'caption': None,
        'comment_muted': int,
        'media_header_display': str,
    }
