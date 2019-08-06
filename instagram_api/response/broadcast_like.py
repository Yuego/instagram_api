from .base_response import Response

__all__ = ['BroadcastLikeResponse']


class BroadcastLikeResponse(Response):
    JSON_PROPERTY_MAP = {
        'likes': None,
    }
