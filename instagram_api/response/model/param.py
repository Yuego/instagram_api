from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['Param']


class Param(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'name': None,
        'value': None,
    }
