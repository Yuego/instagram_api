from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .args import Args
from .counts import Counts

__all__ = ['Story', 'StoryInterface']


class StoryInterface(ApiInterfaceBase):
    pk: int
    counts: Counts
    args: Args
    type: int
    story_type: int


class Story(PropertyMapper, StoryInterface):
    pass
