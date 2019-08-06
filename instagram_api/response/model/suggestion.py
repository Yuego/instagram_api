from instagram_api.property_mapper import PropertyMapperBase

from .user import User

__all__ = ['Suggestion']


class Suggestion(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'media_infos': None,
        'social_context': str,
        'algorithm': str,
        'thumbnail_urls': [str],
        'value': float,
        'caption': None,
        'user': User,
        'large_urls': [str],
        'media_ids': None,
        'icon': None,
        'is_new_suggestion': bool,
        'uuid': str,
    }
