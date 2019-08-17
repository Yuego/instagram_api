from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['PostLiveLikesResponse']


class PostLiveLikesResponseInterface(ApiResponseInterface):
    starting_offset: AnyType
    ending_offset: AnyType
    next_fetch_offset: AnyType
    time_series: AnyType


class PostLiveLikesResponse(ApiResponse, PostLiveLikesResponseInterface):
    pass
