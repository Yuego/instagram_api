from .base_response import ApiResponse

__all__ = ['MediaDeleteResponse']


class MediaDeleteResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'did_delete': None,
    }
