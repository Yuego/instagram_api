from instagram_api.property_mapper import PropertyMapperBase

from instagram_api.property_mapper.types import timestamp

from .user import User

__all__ = ['Comment']


class Comment(PropertyMapperBase):
    PARENT = 0
    CHILD = 2

    JSON_PROPERTY_MAP = {
        'status': str,
        'user_id': int,
        'created_at': timestamp,
        'created_at_utc': timestamp,

        'bit_flags': int,
        'user': User,
        'pk': str,
        'media_id': int,
        'text': str,
        'content_type': str,

        'type': int,
        'comment_like_count': int,
        'has_liked_comment': bool,
        'has_translation': bool,
        'did_report_as_spam': bool,

        'parent_comment_id': int,

        'child_comment_count': int,

        'preview_child_comments': ['self'],

        'other_preview_users': [User],
        'inline_composer_display_condition': str,

        'has_more_tail_child_comments': bool,
        'next_max_child_cursor': str,
        'num_tail_child_comments': int,
        'has_more_head_child_comments': bool,
        'next_min_child_cursor': str,
        'num_head_child_comments': int,
    }
