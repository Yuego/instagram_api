from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import User

__all__ = ['PostLiveViewerListResponse']


class PostLiveViewerListResponseInterface(ApiResponseInterface):
    users: [User]
    next_max_id: str
    total_viewer_count: int


class PostLiveViewerListResponse(ApiResponse, PostLiveViewerListResponseInterface):
    pass
