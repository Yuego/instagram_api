from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['Hashtag']


class Hashtag(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'id': int,
        'name': str,
        'media_count': int,
        'profile_pic_url': str,
        'follow_status': int,
        'following': int,
        'allow_following': int,
        'allow_muting_story': bool,
        'related_tags': None,
        'debug_info': None,
    }
