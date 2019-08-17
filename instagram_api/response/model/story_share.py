from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .item import Item

__all__ = ['StoryShare', 'StoryShareInterface']


class StoryShareInterface(ApiInterfaceBase):
    media: Item
    text: str
    title: str
    message: str
    is_linked: bool


class StoryShare(PropertyMapper, StoryShareInterface):
    pass
