from instagram_api.property_mapper import PropertyMapperBase

from .action import Action
from .image import Image
from .text import Text

__all__ = ['Creative']


class Creative(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'title': Text,
        'content': Text,
        'footer': Text,
        'social_context': Text,
        'primary_action': Action,
        'secondary_action': Action,
        'dismiss_action': None,
        'image': Image,
    }
