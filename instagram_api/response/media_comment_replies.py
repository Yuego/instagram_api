from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import Comment

__all__ = ['MediaCommentRepliesResponse']


class MediaCommentRepliesResponseInterface(ApiResponseInterface):
    parent_comment: Comment
    child_comment_count: int
    child_comments: [Comment]
    has_more_tail_child_comments: bool
    next_max_child_cursor: str
    num_tail_child_comments: int
    has_more_head_child_comments: bool
    next_min_child_cursor: str
    num_head_child_comments: int


class MediaCommentRepliesResponse(ApiResponse, MediaCommentRepliesResponseInterface):
    pass
