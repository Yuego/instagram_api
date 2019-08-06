from .base_response import Response
from .model import PushSettings

__all__ = ['PushPreferencesResponse']


class PushPreferencesResponse(Response):
    JSON_PROPERTY_MAP = {
        'push_settings': [PushSettings],
        'likes': None,
        'comments': None,
        'comment_likes': None,
        'like_and_comment_on_photo_user_tagged': None,
        'live_broadcast': None,
        'new_follower': None,
        'follow_request_accepted': None,
        'contact_joined': None,
        'pending_direct_share': None,
        'direct_share_activity': None,
        'user_tagged': None,
        'notification_reminders': None,
        'first_post': None,
        'announcements': None,
        'ads': None,
        'view_count': None,
        'report_updated': None,
    }
