from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .broadcast import Broadcast

__all__ = ['LiveVideoShare', 'LiveVideoShareInterface']


class LiveVideoShareInterface(ApiInterfaceBase):
    text: str
    broadcast: Broadcast
    video_offset: int


class LiveVideoShare(PropertyMapper, LiveVideoShareInterface):
    pass
