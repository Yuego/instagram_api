from .base_response import Response

__all__ = ['RecoveryResponse']


class RecoveryResponse(Response):
    JSON_PROPERTY_MAP = {
        'phone_number_valid': bool,
        'title': str,
        'body': str,
    }
