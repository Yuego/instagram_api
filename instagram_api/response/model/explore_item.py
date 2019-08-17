from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .channel import Channel
from .explore_item_info import ExploreItemInfo
from .item import Item
from .stories import Stories

__all__ = ['ExploreItem', 'ExploreItemInterface']


class ExploreItemInterface(ApiInterfaceBase):
    media: Item
    stories: Stories
    channel: Channel
    explore_item_info: ExploreItemInfo


class ExploreItem(PropertyMapper, ExploreItemInterface):
    pass
