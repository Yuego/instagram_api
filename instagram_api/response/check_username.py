from .base_response import Response

__all__ = ['CheckUsernameResponse']


class CheckUsernameResponse(Response):
    JSON_PROPERTY_MAP = {
        'username': str,
        'available': None,
        'error': None,
        'error_type': None,
    }
