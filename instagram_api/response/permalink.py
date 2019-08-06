from .base_response import Response

__all__ = ['PermalinkResponse']


class PermalinkResponse(Response):
    JSON_PROPERTY_MAP = {
        'permalink': str,
    }
