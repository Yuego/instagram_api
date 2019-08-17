from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .bold import Bold

__all__ = ['ActionLog', 'ActionLogInterface']


class ActionLogInterface(ApiInterfaceBase):
    bold: [Bold]
    description: str


class ActionLog(PropertyMapper, ActionLogInterface):
    pass
