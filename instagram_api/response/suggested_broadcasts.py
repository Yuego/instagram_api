from .base_response import ApiResponse
from .model import Broadcast

__all__ = ['SuggestedBroadcastsResponse']


class SuggestedBroadcastsResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'broadcasts': [Broadcast],
    }
