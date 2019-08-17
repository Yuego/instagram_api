from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .stickers import Stickers

__all__ = ['StaticStickers', 'StaticStickersInterface']


class StaticStickersInterface(ApiInterfaceBase):
    include_in_recent: AnyType
    id: int
    stickers: [Stickers]


class StaticStickers(PropertyMapper, StaticStickersInterface):
    pass
