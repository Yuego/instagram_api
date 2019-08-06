from .base_response import Response
from .model import Item, User

__all__ = ['ReelMediaVideoResponse']


class ReelMediaVideoResponse(Response):
    JSON_PROPERTY_MAP = {
        'users': [User],
        'next_max_id': str,
        'user_count': int,
        'total_viewer_count': int,
        'screenshotter_user_ids': None,
        'total_screenshot_count': int,
        'updated_media': Item,
    }
