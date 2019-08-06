from .base_response import Response
from .model import BlockedReels

__all__ = ['ReelSettingsResponse']


class ReelSettingsResponse(Response):
    JSON_PROPERTY_MAP = {
        'message_prefs': None,
        'blocked_reels': BlockedReels,
    }
