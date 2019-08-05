from instagram_api.property_mapper import PropertyMapperBase

from .user import User

__all__ = ['Responder']


class Responder(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'response': str,
        'has_shared_response': bool,
        'id': str,
        'user': User,
        'ts': int,
    }
