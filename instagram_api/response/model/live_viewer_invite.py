from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .broadcast import Broadcast

__all__ = ['LiveViewerInvite', 'LiveViewerInviteInterface']


class LiveViewerInviteInterface(ApiInterfaceBase):
    text: str
    broadcast: Broadcast
    title: str
    message: str


class LiveViewerInvite(PropertyMapper, LiveViewerInviteInterface):
    pass
