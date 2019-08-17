from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['TimeRange', 'TimeRangeInterface']


class TimeRangeInterface(ApiInterfaceBase):
    start: int
    end: int


class TimeRange(PropertyMapper, TimeRangeInterface):
    pass

