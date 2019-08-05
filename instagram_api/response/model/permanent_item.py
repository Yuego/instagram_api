from instagram_api.property_mapper import PropertyMapperBase

from .item import Item
from .link import Link
from .live_video_share import LiveVideoShare
from .location import Location
from .media_data import MediaData
from .reel_share import ReelShare
from .user import User

__all__ = ['PermanentItem']


class PermanentItem(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'item_id': int,
        'user_id': int,
        'timestamp': int,
        'item_type': str,
        'profile': User,
        'text': str,
        'location': Location,
        'like': None,
        'media': MediaData,
        'link': Link,
        'media_share': Item,
        'reel_share': ReelShare,
        'client_context': str,
        'live_video_share': LiveVideoShare,
    }
