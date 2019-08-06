from instagram_api.property_mapper import PropertyMapperBase

from .story_tray import StoryTray

__all__ = ['TraySuggestions']


class TraySuggestions(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'tray': [StoryTray],
        'tray_title': str,
        'banner_title': str,
        'banner_subtitle': str,
        'suggestion_type': str,
    }
