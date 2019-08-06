from instagram_api.property_mapper import PropertyMapperBase

from .user import User

__all__ = ['UserCard']


class UserCard(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'user': User,
        'algorithm': str,
        'social_context': str,
        'caption': None,
        'icon': None,
        'media_ids': None,
        'thumbnail_urls': None,
        'large_urls': None,
        'media_infos': None,
        'value': float,
        'is_new_suggestion': bool,
        'uuid': str,
        'followed_by': bool,
    }
