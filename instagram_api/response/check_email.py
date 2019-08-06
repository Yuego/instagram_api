from .base_response import Response

__all__ = ['CheckEmailResponse']


class CheckEmailResponse(Response):
    JSON_PROPERTY_MAP = {
        'valid': None,
        'available': None,
        'confirmed': None,
        'username_suggestions': [str],
        'error_type': None,
    }
