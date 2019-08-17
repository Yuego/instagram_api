from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import Story

__all__ = ['FollowingRecentActivityResponse']


class FollowingRecentActivityResponseInterface(ApiResponseInterface):
    stories: [Story]
    next_max_id: str
    auto_load_more_enabled: AnyType
    megaphone: AnyType


class FollowingRecentActivityResponse(ApiResponse, FollowingRecentActivityResponseInterface):
    pass
