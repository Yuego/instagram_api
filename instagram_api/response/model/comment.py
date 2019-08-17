from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType, Lazy

from .user import User

__all__ = ['Comment', 'CommentInterface']


class CommentInterface(ApiInterfaceBase):
    PARENT = 0
    CHILD = 2

    status: str
    user_id: int
    created_at: Timestamp
    created_at_utc: Timestamp

    bit_flags: int
    user: User
    pk: str
    media_id: int
    text: str
    content_type: str

    type: int
    comment_like_count: int
    has_liked_comment: bool
    has_translation: bool
    did_report_as_spam: bool

    parent_comment_id: int

    child_comment_count: int

    preview_child_comments: Lazy.model__comment__Comment

    other_preview_users: [User]
    inline_composer_display_condition: str

    has_more_tail_child_comments: bool
    next_max_child_cursor: str
    num_tail_child_comments: int
    has_more_head_child_comments: bool
    next_min_child_cursor: str
    num_head_child_comments: int


class Comment(PropertyMapper, CommentInterface):
    pass
