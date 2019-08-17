from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['Param', 'ParamInterface']


class ParamInterface(ApiInterfaceBase):
    name: AnyType
    value: AnyType


class Param(PropertyMapper, ParamInterface):
    pass
