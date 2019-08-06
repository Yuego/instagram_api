from .base_response import Response
from .model import Reel

__all__ = ['ReelsMediaResponse']


class ReelsMediaResponse(Response):
    JSON_PROPERTY_MAP = {
        'reels_media': [Reel],
        'reels': 'Model\UnpredictableKeys\ReelUnpredictableContainer',
    }
