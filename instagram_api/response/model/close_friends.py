from instagram_api.property_mapper import PropertyMapperBase

from .user import User

__all__ = ['CloseFriends']


class CloseFriends(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'sections': None,
        'users': [User],
        'big_list': None,
        'page_size': None,
    }
