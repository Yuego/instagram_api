from instagram_api.property_mapper import PropertyMapperBase

from .item import Item

__all__ = ['Groups']


class Groups(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'type': None,
        'items': [Item],
    }
