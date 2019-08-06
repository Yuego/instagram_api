from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['Template']


class Template(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'name': str,
        'parameters': None,
    }
