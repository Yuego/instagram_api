from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['HideReason', 'HideReasonInterface']


class HideReasonInterface(ApiInterfaceBase):
    text: str
    reason: str


class HideReason(PropertyMapper, HideReasonInterface):
    pass
