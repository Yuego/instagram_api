from .base_response import ApiResponse

__all__ = ['CheckUsernameResponse']


class CheckUsernameResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'username': str,
        'available': None,
        'error': None,
        'error_type': None,
    }
