from .base_response import Response

__all__ = ['MediaDeleteResponse']


class MediaDeleteResponse(Response):
    JSON_PROPERTY_MAP = {
        'did_delete': None,
    }
