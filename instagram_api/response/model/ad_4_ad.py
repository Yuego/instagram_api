from instagram_api.property_mapper import PropertyMapperBase

from .item import Item

__all__ = ['Ad4ad']


class Ad4ad(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'type': None,
        'title': str,
        'media': Item,
        'footer': None,
        'id': str,
        'tracking_token': str,
    }
