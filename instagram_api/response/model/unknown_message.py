from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['UnknownMessage']


class UnknownMessage(PropertyMapperBase):

    JSON_PROPERTY_MAP = {
        'key': str,
        'time': str,
    }
