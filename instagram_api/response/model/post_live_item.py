from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .broadcast import Broadcast
from .user import User

__all__ = ['PostLiveItem', 'PostLiveItemInterface']


class PostLiveItemInterface(ApiInterfaceBase):
    pk: int
    user: User
    broadcasts: [Broadcast]
    peak_viewer_count: int
    last_seen_broadcast_ts: Timestamp
    can_reply: AnyType
    ranked_position: AnyType
    seen_ranked_position: AnyType
    muted: AnyType
    can_reshare: AnyType


class PostLiveItem(PropertyMapper, PostLiveItemInterface):
    pass
