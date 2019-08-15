from .base_response import ApiResponse
from .model import BroadcastStatusItem

__all__ = ['TopLiveStatusResponse']


class TopLiveStatusResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'broadcast_status_items': [BroadcastStatusItem],
    }
