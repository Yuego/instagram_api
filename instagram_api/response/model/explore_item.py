from instagram_api.property_mapper import PropertyMapperBase

from .channel import Channel
from .explore_item_info import ExploreItemInfo
from .item import Item
from .stories import Stories

__all__ = ['ExploreItem']


class ExploreItem(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'media': Item,
        'stories': Stories,
        'channel': Channel,
        'explore_item_info': ExploreItemInfo,
    }
