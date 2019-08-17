from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['Nametag', 'NametagInterface']


class NametagInterface(ApiInterfaceBase):
    mode: int
    gradient: int
    emoji: str
    selfie_sticker: int


class Nametag(PropertyMapper, NametagInterface):
    pass

