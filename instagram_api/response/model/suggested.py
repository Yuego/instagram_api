from instagram_api.property_mapper import PropertyMapperBase

from .location_item import LocationItem
from .hashtag import Hashtag
from .user import User

__all__ = ['Suggested']


class Suggested(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'position': int,
        'hashtag': Hashtag,
        'user': User,
        'place': LocationItem,
        'client_time': None,
    }
