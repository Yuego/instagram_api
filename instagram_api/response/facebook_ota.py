from .base_response import ApiResponse

__all__ = ['FacebookOTAResponse']


class FacebookOTAResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'bundles': None,
        'request_id': str,
    }
