from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['Placeholder']


class Placeholder(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'is_linked': bool,
        'title': str,
        'message': str,
    }
