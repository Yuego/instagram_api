from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import Comment

__all__ = ['BroadcastCommentsResponse']


class BroadcastCommentsResponseInterface(ApiResponseInterface):
    comments: [Comment]
    comment_count: int
    live_seconds_per_comment: int
    has_more_headload_comments: bool
    is_first_fetch: str
    comment_likes_enabled: bool
    pinned_comment: Comment
    system_comments: [Comment]
    has_more_comments: bool
    caption_is_edited: bool
    caption: AnyType
    comment_muted: int
    media_header_display: str


class BroadcastCommentsResponse(ApiResponse, BroadcastCommentsResponseInterface):
    pass
