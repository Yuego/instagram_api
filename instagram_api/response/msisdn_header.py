from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['MsisdnHeaderResponse']


class MsisdnHeaderResponseInterface(ApiResponseInterface):
    phone_number: str
    url: str
    remaining_ttl_seconds: int
    ttl: int


class MsisdnHeaderResponse(ApiResponse, MsisdnHeaderResponseInterface):
    pass
