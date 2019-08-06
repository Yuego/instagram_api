from .base_response import Response
from .model import User

__all__ = ['PostLiveViewerListResponse']


class PostLiveViewerListResponse(Response):
    JSON_PROPERTY_MAP = {
        'users': [User],
        'next_max_id': str,
        'total_viewer_count': int,
    }
