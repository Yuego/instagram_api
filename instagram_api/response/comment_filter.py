from .base_response import ApiResponse

__all__ = ['CommentFilterResponse']


class CommentFilterResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'config_value': None,
    }
