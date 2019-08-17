from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import SuggestedUsers, User

__all__ = ['FollowerAndFollowingResponse']


class FollowerAndFollowingResponseInterface(ApiResponseInterface):
    users: [User]
    suggested_users: SuggestedUsers
    truncate_follow_requests_at_index: int
    next_max_id: str
    page_size: AnyType
    big_list: bool


class FollowerAndFollowingResponse(ApiResponse, FollowerAndFollowingResponseInterface):
    pass
