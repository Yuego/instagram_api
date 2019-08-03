from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['Gating']


class Gating(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'gating_type': None,
        'description': None,
        'buttons': None,
        'title': None,
    }
