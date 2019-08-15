from .base_response import ApiResponse
from .model import User

__all__ = ['BroadcastLikeCountResponse']


class BroadcastLikeCountResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'like_ts': int,
        'likes': int,
        'burst_likes': int,
        'likers': [User],
    }
