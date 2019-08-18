from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import Caption, Comment

__all__ = ['MediaCommentsResponse']


class MediaCommentsResponseInterface(ApiResponseInterface):
    comments: [Comment]
    comment_count: int
    comment_likes_enabled: bool
    next_max_id: str
    next_min_id: str
    caption: Caption
    has_more_comments: bool
    caption_is_edited: bool
    preview_comments: AnyType
    has_more_headload_comments: bool
    media_header_display: str
    threading_enabled: bool


class MediaCommentsResponse(ApiResponse, MediaCommentsResponseInterface):
    pass
