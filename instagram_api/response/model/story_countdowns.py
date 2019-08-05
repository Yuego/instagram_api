from instagram_api.property_mapper import PropertyMapperBase

from .countdown_sticker import CountdownSticker

__all__ = ['StoryCountdowns']


class StoryCountdowns(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'x': float,
        'y': float,
        'z': float,
        'width': float,
        'height': float,
        'rotation': float,
        'is_pinned': int,
        'is_hidden': int,
        'countdown_sticker': CountdownSticker,
    }
