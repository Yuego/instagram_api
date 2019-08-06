from .base_response import Response

__all__ = ['StartLiveResponse']


class StartLiveResponse(Response):
    JSON_PROPERTY_MAP = {
        'media_id': int,
    }
