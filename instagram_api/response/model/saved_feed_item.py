from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .item import Item

__all__ = ['SavedFeedItem', 'SavedFeedItemInterface']


class SavedFeedItemInterface(ApiInterfaceBase):
    media: Item


class SavedFeedItem(PropertyMapper, SavedFeedItemInterface):
    pass
