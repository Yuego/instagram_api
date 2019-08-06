from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['Tab']


class Tab(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'type': str,
        'title': str,
    }
