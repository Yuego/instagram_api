from instagram_api.property_mapper import PropertyMapperBase

from .user import User

__all__ = ['BlockedReels']


class BlockedReels(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'users': [User],
        'page_size': None,
        'big_list': bool,
    }
