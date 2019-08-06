from .base_response import Response

__all__ = ['PinCommentBroadcastResponse']


class PinCommentBroadcastResponse(Response):
    JSON_PROPERTY_MAP = {
        'comment_id': int,
    }
