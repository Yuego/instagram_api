from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import Item, User

__all__ = ['ReelMediaViewerResponse']


class ReelMediaViewerResponseInterface(ApiResponseInterface):
    users: [User]
    next_max_id: str
    user_count: int
    total_viewer_count: int
    screenshotter_user_ids: AnyType
    total_screenshot_count: int
    updated_media: Item


class ReelMediaViewerResponse(ApiResponse, ReelMediaViewerResponseInterface):
    pass
