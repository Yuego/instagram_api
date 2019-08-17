from ..mapper import PropertyMapper

from .common.sticker import StickerInterface

from .hashtag import Hashtag

__all__ = ['StoryHashtag', 'StoryHashtagInterface']


class StoryHashtagInterface(StickerInterface):
    hashtag: Hashtag
    attribution: str
    custom_title: str
    is_hidden: int


class StoryHashtag(PropertyMapper, StoryHashtagInterface):
    pass
