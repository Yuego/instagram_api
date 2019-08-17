from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .item import Item

__all__ = ['FelixShare', 'FelixShareInterface']


class FelixShareInterface(ApiInterfaceBase):
    video: [Item]
    text: str


class FelixShare(PropertyMapper, FelixShareInterface):
    pass
