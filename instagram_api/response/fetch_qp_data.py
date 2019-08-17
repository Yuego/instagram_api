from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import QPExtraInfo, QPData

__all__ = ['FetchQPDataResponse']


class FetchQPDataResponseInterface(ApiResponseInterface):
    request_status: str
    extra_info: [QPExtraInfo]
    qp_data: [QPData]
    client_cache_ttl_in_sec: int
    error_msg: AnyType


class FetchQPDataResponse(ApiResponse, FetchQPDataResponseInterface):
    pass
