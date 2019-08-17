from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType


class EnableDisableLiveCommentsResponseInterface(ApiResponseInterface):
    comment_muted: int


class EnableDisableLiveCommentsResponse(ApiResponse, EnableDisableLiveCommentsResponseInterface):
    pass
