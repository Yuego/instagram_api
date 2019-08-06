from .base_response import Response
from .model import Reel

__all__ = ['ActiveReelAdsResponse']


class ActiveReelAdsResponse(Response):
    JSON_PROPERTY_MAP = {
        'reels': [Reel],
        'next_max_id': str,
        'more_available': bool,
    }
