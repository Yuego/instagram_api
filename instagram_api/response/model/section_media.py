from instagram_api.property_mapper import PropertyMapperBase

from .item import Item

__all__ = ['SectionMedia']


class SectionMedia(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'media': Item,
    }
