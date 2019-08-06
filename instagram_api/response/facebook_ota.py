from .base_response import Response

__all__ = ['FacebookOTAResponse']


class FacebookOTAResponse(Response):
    JSON_PROPERTY_MAP = {
        'bundles': None,
        'request_id': str,
    }
