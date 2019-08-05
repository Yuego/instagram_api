from instagram_api.property_mapper import PropertyMapperBase

from .item import Item

__all__ = ['StoryShare']


class StoryShare(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'media': Item,
        'text': str,
        'title': str,
        'message': str,
        'is_linked': bool,
    }
