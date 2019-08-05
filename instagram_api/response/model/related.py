from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['Related']


class Related(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'name': None,
        'id': int,
        'type': None,
    }
