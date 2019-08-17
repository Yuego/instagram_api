from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['BroadcastStatusItem', 'BroadcastStatusItemInterface']


class BroadcastStatusItemInterface(ApiInterfaceBase):
    broadcast_status: str
    has_reduced_visibility: bool
    cover_frame_url: str
    viewer_count: int
    id: int


class BroadcastStatusItem(PropertyMapper, BroadcastStatusItemInterface):
    pass
