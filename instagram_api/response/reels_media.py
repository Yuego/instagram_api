from .base_response import ApiResponse
from .model import Reel

__all__ = ['ReelsMediaResponse']


class ReelsMediaResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'reels_media': [Reel],
        'reels': 'Model\UnpredictableKeys\ReelUnpredictableContainer',
    }
