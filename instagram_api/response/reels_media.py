from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import Reel
from .model.unpredictable import ReelUnpredictableContainer

__all__ = ['ReelsMediaResponse']


class ReelsMediaResponseInterface(ApiResponseInterface):
    reels_media: [Reel]
    reels: ReelUnpredictableContainer


class ReelsMediaResponse(ApiResponse, ReelsMediaResponseInterface):
    pass
