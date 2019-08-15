from .base_response import ApiResponse
from .model import Reel

__all__ = ['UserReelMediaFeedResponse']


class UserReelMediaFeedResponse(ApiResponse, Reel):
    JSON_PROPERTY_MAP = {

    }
