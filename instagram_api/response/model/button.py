from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['Button', 'ButtonInterface']


class ButtonInterface(ApiInterfaceBase):
    text: str
    url: str
    action: AnyType
    background_color: AnyType
    border_color: AnyType
    text_color: AnyType
    action_info: AnyType


class Button(PropertyMapper, ButtonInterface):
    pass
