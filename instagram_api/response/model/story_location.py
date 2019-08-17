from ..mapper import PropertyMapper

from .common.sticker import StickerInterface

from .location import Location

__all__ = ['StoryLocation', 'StoryLocationInterface']


class StoryLocationInterface(StickerInterface):
    location: Location
    attribution: str
    is_hidden: int


class StoryLocation(PropertyMapper, StoryLocationInterface):
    pass
