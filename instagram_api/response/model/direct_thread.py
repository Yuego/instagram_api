from instagram_api.property_mapper import PropertyMapperBase

from .action_badge import ActionBadge
from .direct_thread_item import DirectThreadItem
from .permanent_item import PermanentItem
# from .unpredictable import DirectThreadLastSeenAtUnpredictableContainer
from .user import User

__all__ = ['DirectThread']


class DirectThread(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'thread_id': int,
        'thread_v2_id': int,
        'users': [User],
        'left_users': [User],
        'items': [DirectThreadItem],
        'last_activity_at': str,
        'muted': bool,
        'is_pin': bool,
        'named': bool,
        'canonical': bool,
        'pending': bool,
        'valued_request': bool,
        'thread_type': str,
        'viewer_id': int,
        'thread_title': str,
        'pending_score': str,
        'vc_muted': bool,
        'is_group': bool,
        'reshare_send_count': int,
        'reshare_receive_count': int,
        'expiring_media_send_count': int,
        'expiring_media_receive_count': int,
        'inviter': User,
        'has_older': bool,
        'has_newer': bool,
        # 'last_seen_at': DirectThreadLastSeenAtUnpredictableContainer,
        'newest_cursor': str,
        'oldest_cursor': str,
        'is_spam': bool,
        'last_permanent_item': PermanentItem,
        'unseen_count': None,
        'action_badge': ActionBadge,
        'last_activity_at_secs': None,
    }
