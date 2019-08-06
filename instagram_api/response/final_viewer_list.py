from .base_response import Response
from .model import User

__all__ = ['FinalViewerListResponse']


class FinalViewerListResponse(Response):
    JSON_PROPERTY_MAP = {
        'users': [User],
        'total_unique_viewer_count': 'int',
    }
