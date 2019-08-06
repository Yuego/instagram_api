from .base_response import Response
from .model import BroadcastStatusItem

__all__ = ['TopLiveStatusResponse']


class TopLiveStatusResponse(Response):
    JSON_PROPERTY_MAP = {
        'broadcast_status_items': [BroadcastStatusItem],
    }
