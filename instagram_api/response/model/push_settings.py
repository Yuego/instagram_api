from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['PushSettings', 'PushSettingsInterface']


class PushSettingsInterface(ApiInterfaceBase):
    name: AnyType
    eligible: AnyType
    title: AnyType
    example: AnyType
    options: AnyType
    checked: AnyType


class PushSettings(PropertyMapper, PushSettingsInterface):
    pass
