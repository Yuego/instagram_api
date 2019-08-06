from .base_response import Response
from .model import User

__all__ = ['BroadcastLikeCountResponse']


class BroadcastLikeCountResponse(Response):
    JSON_PROPERTY_MAP = {
        'like_ts': int,
        'likes': int,
        'burst_likes': int,
        'likers': [User],
    }
