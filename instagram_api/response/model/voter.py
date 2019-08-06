from instagram_api.property_mapper import PropertyMapperBase

from .user import User

__all__ = ['Voter']


class Voter(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'user': User,
        'vote': int,
    }
