from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['PushSettings']


class PushSettings(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'name': None,
        'eligible': None,
        'title': None,
        'example': None,
        'options': None,
        'checked': None,
    }
