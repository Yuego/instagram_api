from instagram_api.property_mapper import PropertyMapperBase

from .user import User

__all__ = ['UserList']


class UserList(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'position': int,
        'user': User,
    }
