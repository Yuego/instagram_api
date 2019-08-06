from .base_response import Response
from .model import SystemControl, TraceControl

__all__ = ['LoomFetchConfigResponse']


class LoomFetchConfigResponse(Response):
    JSON_PROPERTY_MAP = {
        'system_control': SystemControl,
        'trace_control': TraceControl,
        'id': int,
    }
