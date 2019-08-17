from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['Gating', 'GatingInterface']


class GatingInterface(ApiInterfaceBase):
    gating_type: AnyType
    description: AnyType
    buttons: AnyType
    title: AnyType


class Gating(PropertyMapper, GatingInterface):
    pass
