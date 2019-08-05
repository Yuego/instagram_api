from instagram_api.property_mapper import PropertyMapperBase

from .business_manager import BusinessManager
from .image import Image

__all__ = ['ShadowInstagramUser']


class ShadowInstagramUser(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'id': int,
        'instagram_user_id': int,
        'followers_count': int,
        'username': str,
        'profile_picture': Image,
        'business_manager': BusinessManager,
        'error': None,
    }
