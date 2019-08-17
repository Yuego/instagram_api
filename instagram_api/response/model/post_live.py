from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .post_live_item import PostLiveItem

__all__ = ['PostLive', 'PostLiveInterface']


class PostLiveInterface(ApiInterfaceBase):
    post_live_items: [PostLiveItem]


class PostLive(PropertyMapper, PostLiveInterface):
    pass
