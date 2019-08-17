from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .item import Item
from .link import Link
from .live_video_share import LiveVideoShare
from .location import Location
from .media_data import MediaData
from .reel_share import ReelShare
from .user import User

__all__ = ['PermanentItem', 'PermanentItemInterface']


class PermanentItemInterface(ApiInterfaceBase):
    item_id: int
    user_id: int
    timestamp: int
    item_type: str
    profile: User
    text: str
    location: Location
    like: AnyType
    media: MediaData
    link: Link
    media_share: Item
    reel_share: ReelShare
    client_context: str
    live_video_share: LiveVideoShare


class PermanentItem(PropertyMapper, PermanentItemInterface):
    pass
