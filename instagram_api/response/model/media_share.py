from instagram_api.property_mapper import PropertyMapperBase

from .item import Item

__all__ = ['Item']


class MediaShare(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'media': Item,
        'text': str,
    }
