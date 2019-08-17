from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import User

__all__ = ['FinalViewerListResponse']


class FinalViewerListResponseInterface(ApiResponseInterface):
    users: [User]
    total_unique_viewer_count: int


class FinalViewerListResponse(ApiResponse, FinalViewerListResponseInterface):
    pass
