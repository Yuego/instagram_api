from .base_response import ApiResponse
from .model import DirectThreadItem, User

__all__ = ['DirectCreateGroupThread']


class DirectCreateGroupThread(ApiResponse):
    JSON_PROPERTY_MAP = {
        'thread_id': int,
        'users': [User],
        'left_users': [User],
        'items': [DirectThreadItem],
        'last_activity_at': None,
        'muted': None,
        'named': None,
        'canonical': None,
        'pending': None,
        'thread_type': None,
        'viewer_id': str,
        'thread_title': None,
        'inviter': User,
        'has_older': bool,
        'has_newer': bool,
        'last_seen_at': None,
        'is_pin': None,
    }
