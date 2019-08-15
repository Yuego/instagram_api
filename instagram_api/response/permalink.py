from .base_response import ApiResponse

__all__ = ['PermalinkResponse']


class PermalinkResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'permalink': str,
    }
