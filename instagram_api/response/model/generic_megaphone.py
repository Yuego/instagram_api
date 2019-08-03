from instagram_api.property_mapper import PropertyMapperBase

from .button import Button

__all__ = ['GenericMegaphone']


class GenericMegaphone(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'type': None,
        'title': None,
        'message': None,
        'dismissible': None,
        'icon': None,
        'buttons': [Button],
        'megaphone_version': None,
        'button_layout': None,
        'action_info': None,
        'button_location': None,
        'background_color': None,
        'title_color': None,
        'message_color': None,
        'uuid': str,
    }
