from instagram_api.property_mapper import PropertyMapperBase

from .item import Item

__all__ = ['Channel']


class Channel(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'channel_id': int,
        'channel_type': None,
        'title': None,
        'header': None,
        'media_count': int,
        'media': Item,
        'context': None,
    }
