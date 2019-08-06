from .base_response import Response
from .model import QPExtraInfo, QPData

__all__ = ['FetchQPDataResponse']


class FetchQPDataResponse(Response):
    JSON_PROPERTY_MAP = {
        'request_status': str,
        'extra_info': [QPExtraInfo],
        'qp_data': [QPData],
        'client_cache_ttl_in_sec': int,
        'error_msg': None,
    }
