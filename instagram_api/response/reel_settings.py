from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import BlockedReels

__all__ = ['ReelSettingsResponse']


class ReelSettingsResponseInterface(ApiResponseInterface):
    message_prefs: AnyType
    blocked_reels: BlockedReels


class ReelSettingsResponse(ApiResponse, ReelSettingsResponseInterface):
    pass
