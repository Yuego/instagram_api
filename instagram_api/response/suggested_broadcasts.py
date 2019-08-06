from .base_response import Response
from .model import Broadcast

__all__ = ['SuggestedBroadcastsResponse']


class SuggestedBroadcastsResponse(Response):
    JSON_PROPERTY_MAP = {
        'broadcasts': [Broadcast],
    }
