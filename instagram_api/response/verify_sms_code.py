from .base_response import ApiResponse

__all__ = ['VerifySMSCodeResponse']


class VerifySMSCodeResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'verified': bool,
        'phone_number': str,
    }
