from instagram_api.property_mapper import PropertyMapperBase

from .aymf_item import AymfItem

__all__ = ['Aymf']


class Aymf(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'items': [AymfItem],
        'more_available': bool,
    }
