from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import Reel

__all__ = ['ActiveReelAdsResponse']


class ActiveReelAdsResponseInterface(ApiResponseInterface):
    reels: [Reel]
    next_max_id: str
    more_available: bool


class ActiveReelAdsResponse(ApiResponse, ApiResponseInterface):
    pass
