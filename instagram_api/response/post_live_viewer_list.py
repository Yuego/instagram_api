from .base_response import ApiResponse
from .model import User

__all__ = ['PostLiveViewerListResponse']


class PostLiveViewerListResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'users': [User],
        'next_max_id': str,
        'total_viewer_count': int,
    }
