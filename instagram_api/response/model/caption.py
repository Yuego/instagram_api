from instagram_api.property_mapper import PropertyMapperBase

from .user import User

__all__ = ['Caption']


class Caption(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'status': str,
        'user_id': str,
        'created_at_utc': str,
        'created_at': str,
        'bit_flags': int,
        'user': User,
        'content_type': None,
        'text': str,
        'media_id': str,
        'pk': str,
        'type': int,
        'has_translation': bool,
        'did_report_as_spam': bool,
        'share_enabled': bool,
    }
