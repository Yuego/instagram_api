from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['SharedFollower']


class SharedFollower(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'pk': int,
        'username': str,
        'full_name': str,
        'is_private': bool,
        'profile_pic_url': str,
        'profile_pic_id': int,
        'is_verified': bool,
        'has_anonymous_profile_picture': bool,
        'reel_auto_archive': str,
        'overlap_score': str,
    }
