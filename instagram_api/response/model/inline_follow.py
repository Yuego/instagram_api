from instagram_api.property_mapper import PropertyMapperBase

from .user import User

__all__ = ['InlineFollow']


class InlineFollow(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'user_info': User,
        'following': bool,
        'outgoing_request': bool,
    }
