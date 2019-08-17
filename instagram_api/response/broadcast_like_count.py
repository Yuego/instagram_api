from .mapper import ApiResponse, ApiResponseInterface

from .model import User

__all__ = ['BroadcastLikeCountResponse']


class BroadcastLikeCountResponseInterface(ApiResponseInterface):
    like_ts: int
    likes: int
    burst_likes: int
    likers: [User]


class BroadcastLikeCountResponse(ApiResponse, BroadcastLikeCountResponseInterface):
    pass
