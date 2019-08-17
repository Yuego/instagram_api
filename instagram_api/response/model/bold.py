from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['Bold', 'BoldInterface']


class BoldInterface(ApiInterfaceBase):
    start: int
    end: int


class Bold(PropertyMapper, BoldInterface):
    pass
