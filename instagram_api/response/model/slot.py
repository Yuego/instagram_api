from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['Slot', 'SlotInterface']


class SlotInterface(ApiInterfaceBase):
    slot: int
    cooldown: int


class Slot(PropertyMapper, SlotInterface):
    pass
