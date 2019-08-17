from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .item import Item
from .user import User

__all__ = ['TvChannel', 'TvChannelInterface']


class TvChannelInterface(ApiInterfaceBase):
    type: str
    title: str
    id: str
    items: [Item]
    more_available: str
    max_id: int
    seen_state: AnyType
    user_dict: User


class TvChannel(PropertyMapper, TvChannelInterface):
    pass
