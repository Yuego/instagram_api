from .base_response import Response
from .model import Comment

__all__ = ['MediaCommentRepliesResponse']


class MediaCommentRepliesResponse(Response):
    JSON_PROPERTY_MAP = {
        'parent_comment': Comment,
        'child_comment_count': int,
        'child_comments': [Comment],
        'has_more_tail_child_comments': bool,
        'next_max_child_cursor': str,
        'num_tail_child_comments': int,
        'has_more_head_child_comments': bool,
        'next_min_child_cursor': str,
        'num_head_child_comments': int,
    }
