from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .button import Button

__all__ = ['GenericMegaphone', 'GenericMegaphoneInterface']


class GenericMegaphoneInterface(ApiInterfaceBase):
    type: AnyType
    title: AnyType
    message: AnyType
    dismissible: AnyType
    icon: AnyType
    buttons: [Button]
    megaphone_version: AnyType
    button_layout: AnyType
    action_info: AnyType
    button_location: AnyType
    background_color: AnyType
    title_color: AnyType
    message_color: AnyType
    uuid: str


class GenericMegaphone(PropertyMapper, GenericMegaphoneInterface):
    pass
