from .base_response import Response

__all__ = ['CommentFilterResponse']


class CommentFilterResponse(Response):
    JSON_PROPERTY_MAP = {
        'config_value': None,
    }
