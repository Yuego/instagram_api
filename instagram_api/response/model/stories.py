from instagram_api.property_mapper import PropertyMapperBase

from .story_tray import StoryTray
from .top_live import TopLive

__all__ = ['Stories']


class Stories(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'is_portrait': bool,
        'tray': [StoryTray],
        'id': int,
        'top_live': TopLive,
    }
