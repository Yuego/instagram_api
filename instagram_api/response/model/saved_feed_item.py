from instagram_api.property_mapper import PropertyMapperBase

from .item import Item

__all__ = ['SavedFeedItem']


class SavedFeedItem(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'media': Item,
    }
