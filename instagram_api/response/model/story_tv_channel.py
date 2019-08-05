from instagram_api.property_mapper import PropertyMapperBase

from .item import Item
from .user import User

__all__ = ['StoryTvChannel']


class StoryTvChannel(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'id': int,
        'items': [Item],
        'title': str,
        'type': str,
        'max_id': str,
        'more_available': bool,
        'seen_state': None,
        'user_dict': User,
    }
