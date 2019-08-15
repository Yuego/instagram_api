from .base_response import ApiResponse

__all__ = ['UnpinCommentBroadcastResponse']


class UnpinCommentBroadcastResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'comment_id': int,
    }
