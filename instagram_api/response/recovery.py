from .base_response import ApiResponse

__all__ = ['RecoveryResponse']


class RecoveryResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'phone_number_valid': bool,
        'title': str,
        'body': str,
    }
