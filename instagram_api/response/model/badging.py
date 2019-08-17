from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['Badging', 'BadgingInterface']


class BadgingInterface(ApiInterfaceBase):
    ids: AnyType
    items: AnyType


class Badging(PropertyMapper, BadgingInterface):
    pass
