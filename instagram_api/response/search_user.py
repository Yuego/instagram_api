from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import User

__all__ = ['SearchUserResponse']


class SearchUserResponseInterface(ApiResponseInterface):
    has_more: bool
    num_results: int
    rank_token: str
    users: [User]


class SearchUserResponse(ApiResponse, SearchUserResponseInterface):
    pass
