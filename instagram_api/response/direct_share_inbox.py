from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['DirectShareInboxResponse']


class DirectShareInboxResponseInterface(ApiResponseInterface):
    shares: AnyType
    max_id: str
    new_shares: AnyType
    patches: AnyType
    last_counted_at: AnyType
    new_shares_info: AnyType


class DirectShareInboxResponse(ApiResponse, DirectShareInboxResponseInterface):
    pass
