from .base_response import ApiResponse

__all__ = ['PinCommentBroadcastResponse']


class PinCommentBroadcastResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'comment_id': int,
    }
