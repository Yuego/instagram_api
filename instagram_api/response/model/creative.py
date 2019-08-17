from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .action import Action
from .image import Image
from .text import Text

__all__ = ['Creative', 'CreativeInterface']


class CreativeInterface(ApiInterfaceBase):
    title: Text
    content: Text
    footer: Text
    social_context: Text
    primary_action: Action
    secondary_action: Action
    dismiss_action: AnyType
    image: Image


class Creative(PropertyMapper, CreativeInterface):
    pass
