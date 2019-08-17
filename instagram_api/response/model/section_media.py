from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .item import Item

__all__ = ['SectionMedia', 'SectionMediaInterface']


class SectionMediaInterface(ApiInterfaceBase):
    media: Item


class SectionMedia(PropertyMapper, SectionMediaInterface):
    pass
