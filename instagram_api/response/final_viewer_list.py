from .base_response import ApiResponse
from .model import User

__all__ = ['FinalViewerListResponse']


class FinalViewerListResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'users': [User],
        'total_unique_viewer_count': 'int',
    }
