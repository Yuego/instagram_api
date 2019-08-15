from .base_response import ApiResponse
from .model import BlockedReels

__all__ = ['ReelSettingsResponse']


class ReelSettingsResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'message_prefs': None,
        'blocked_reels': BlockedReels,
    }
