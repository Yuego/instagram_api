from .base_response import ApiResponse
from .model import SystemControl, TraceControl

__all__ = ['LoomFetchConfigResponse']


class LoomFetchConfigResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'system_control': SystemControl,
        'trace_control': TraceControl,
        'id': int,
    }
