from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .item import Item

__all__ = ['MediaShare', 'MediaShareInterface']


class MediaShareInterface(ApiInterfaceBase):
    media: Item
    text: str


class MediaShare(PropertyMapper, MediaShareInterface):
    pass
