from .common.sticker import Sticker

from .location import Location

__all__ = ['StoryLocation']


class StoryLocation(Sticker):
    JSON_PROPERTY_MAP = {
        'location': Location,
        'attribution': str,
        'is_hidden': int,
    }
