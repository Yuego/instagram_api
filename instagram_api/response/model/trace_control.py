from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['TraceControl', 'TraceControlInterface']


class TraceControlInterface(ApiInterfaceBase):
    max_trace_timeout_ms: int


class TraceControl(PropertyMapper, TraceControlInterface):
    pass

