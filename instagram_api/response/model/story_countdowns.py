from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .countdown_sticker import CountdownSticker

__all__ = ['StoryCountdowns', 'StoryCountdownsInterface']


class StoryCountdownsInterface(ApiInterfaceBase):
    x: float
    y: float
    z: float
    width: float
    height: float
    rotation: float
    is_pinned: int
    is_hidden: int
    countdown_sticker: CountdownSticker


class StoryCountdowns(PropertyMapper, StoryCountdownsInterface):
    pass
