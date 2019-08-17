from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import User

__all__ = ['MutedReelsResponse']


class MutedReelsResponseInterface(ApiResponseInterface):
    users: [User]
    next_max_id: str
    page_size: AnyType
    big_list: AnyType


class MutedReelsResponse(ApiResponse, MutedReelsResponseInterface):
    pass
