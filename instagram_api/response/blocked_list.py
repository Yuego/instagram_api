from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import User

__all__ = ['BlockedListResponse']


class BlockedListResponseInterface(ApiResponseInterface):
    blocked_list: [User]
    next_max_id: str
    page_size: AnyType


class BlockedListResponse(ApiResponse, BlockedListResponseInterface):
    pass
