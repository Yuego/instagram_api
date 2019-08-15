from .base_response import ApiResponse

__all__ = ['CheckEmailResponse']


class CheckEmailResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'valid': None,
        'available': None,
        'confirmed': None,
        'username_suggestions': [str],
        'error_type': None,
    }
