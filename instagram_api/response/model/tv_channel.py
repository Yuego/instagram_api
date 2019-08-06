from instagram_api.property_mapper import PropertyMapperBase

from .item import Item
from .user import User

__all__ = ['TVChannel']


class TVChannel(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'type': str,
        'title': str,
        'id': str,
        'items': [Item],
        'more_available': str,
        'max_id': int,
        'seen_state': None,
        'user_dict': User,
    }
