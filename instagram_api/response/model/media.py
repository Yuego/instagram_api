from instagram_api.property_mapper import PropertyMapperBase
from instagram_api.property_mapper.types import timestamp

from .user import User

__all__ = ['Media']


class Media(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'image': str,
        'id': int,
        'user': User,
        'expiring_at': timestamp,
        'comment_threading_enabled': bool,
    }
