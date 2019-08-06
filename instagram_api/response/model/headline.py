from instagram_api.property_mapper import PropertyMapperBase
from instagram_api.property_mapper.types import timestamp

from .user import User

__all__ = ['Headline']


class Headline(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'content_type': None,
        'user': User,
        'user_id': int,
        'pk': str,
        'text': str,
        'type': None,
        'created_at': timestamp,
        'created_at_utc': str,
        'media_id': int,
        'bit_flags': int,
        'status': None,
    }
