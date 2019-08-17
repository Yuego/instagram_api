from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import SystemControl, TraceControl

__all__ = ['LoomFetchConfigResponse']


class LoomFetchConfigResponseInterface(ApiResponseInterface):
    system_control: SystemControl
    trace_control: TraceControl
    id: int


class LoomFetchConfigResponse(ApiResponse, LoomFetchConfigResponseInterface):
    pass
