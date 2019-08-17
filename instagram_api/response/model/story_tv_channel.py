from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .item import Item
from .user import User

__all__ = ['StoryTvChannel', 'StoryTvChannelInterface']


class StoryTvChannelInterface(ApiInterfaceBase):
    id: int
    items: [Item]
    title: str
    type: str
    max_id: int
    more_available: bool
    seen_state: AnyType
    user_dict: User


class StoryTvChannel(PropertyMapper, StoryTvChannelInterface):
    pass
