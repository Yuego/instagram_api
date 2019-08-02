from instagram_api.property_mapper import PropertyMapperBase

from .item import Item

__all__ = ['Collection']


class Collection(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'collection_id': int,
        'collection_name': str,
        'cover_media': Item,
    }
