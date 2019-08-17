from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .story_tray import StoryTray
from .top_live import TopLive

__all__ = ['Stories', 'StoriesInterface']


class StoriesInterface(ApiInterfaceBase):
    is_portrait: bool
    tray: [StoryTray]
    id: int
    top_live: TopLive


class Stories(PropertyMapper, StoriesInterface):
    pass
