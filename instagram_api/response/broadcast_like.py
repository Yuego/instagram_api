from .base_response import ApiResponse

__all__ = ['BroadcastLikeResponse']


class BroadcastLikeResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'likes': None,
    }
