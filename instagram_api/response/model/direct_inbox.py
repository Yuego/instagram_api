from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .direct_thread import DirectThread

__all__ = ['DirectInbox', 'DirectInboxInterface']


class DirectInboxInterface(ApiInterfaceBase):
    has_older: bool
    unseen_count: int
    unseen_count_ts: AnyType
    blended_inbox_enabled: bool
    oldest_cursor: AnyType
    threads: [DirectThread]


class DirectInbox(PropertyMapper, DirectInboxInterface):
    pass
