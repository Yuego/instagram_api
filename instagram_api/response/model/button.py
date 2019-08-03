from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['Button']


class Button(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'text': str,
        'url': str,
        'action': None,
        'background_color': None,
        'border_color': None,
        'text_color': None,
        'action_info': None,
    }
