from instagram_api.property_mapper import PropertyMapperBase
from instagram_api.property_mapper.types import timestamp

from .broadcast import Broadcast
from .user import User

__all__ = ['PostLiveItem']


class PostLiveItem(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'pk': int,
        'user': User,
        'broadcasts': [Broadcast],
        'peak_viewer_count': int,
        'last_seen_broadcast_ts': timestamp,
        'can_reply': None,
        'ranked_position': None,
        'seen_ranked_position': None,
        'muted': None,
        'can_reshare': None,
    }
