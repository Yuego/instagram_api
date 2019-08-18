from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import LiveComment

__all__ = ['PostLiveCommentsResponse']


class PostLiveCommentsResponseInterface(ApiResponseInterface):
    starting_offset: AnyType
    ending_offset: AnyType
    next_fetch_offset: AnyType
    comments: [LiveComment]
    pinned_comments: [LiveComment]


class PostLiveCommentsResponse(ApiResponse, PostLiveCommentsResponseInterface):
    pass
