from .common.sticker import Sticker

from .hashtag import Hashtag

__all__ = ['StoryHashtag']


class StoryHashtag(Sticker):
    JSON_PROPERTY_MAP = {
        'hashtag': Hashtag,
        'attribution': str,
        'custom_title': str,
        'is_hidden': int,
    }
