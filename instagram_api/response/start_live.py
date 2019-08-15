from .base_response import ApiResponse

__all__ = ['StartLiveResponse']


class StartLiveResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'media_id': int,
    }
