from .mapper import ApiResponse

from .model.reel import ReelInterface

__all__ = ['UserReelMediaFeedResponse']


class UserReelMediaFeedResponseInterface(ReelInterface):
    pass


class UserReelMediaFeedResponse(ApiResponse, UserReelMediaFeedResponseInterface):
    pass
