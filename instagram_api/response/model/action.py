from instagram_api.property_mapper import PropertyMapperBase

from .text import Text

__all__ = ['Action']


class Action(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'title': Text,
        'url': str,
        'limit': int,
        'dismiss_promotion': bool,
    }
