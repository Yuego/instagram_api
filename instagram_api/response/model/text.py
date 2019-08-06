from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['Text']


class Text(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'text': str,
    }
