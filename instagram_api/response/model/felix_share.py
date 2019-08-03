from instagram_api.property_mapper import PropertyMapperBase

from .item import Item

__all__ = ['FelixShare']


class FelixShare(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'video': [Item],
        'text': str,
    }
