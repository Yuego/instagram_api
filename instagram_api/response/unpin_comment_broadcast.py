from .base_response import Response

__all__ = ['UnpinCommentBroadcastResponse']


class UnpinCommentBroadcastResponse(Response):
    JSON_PROPERTY_MAP = {
        'comment_id': int,
    }
