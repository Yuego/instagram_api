from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['Attribution']


class Attribution(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'name': str,
    }
