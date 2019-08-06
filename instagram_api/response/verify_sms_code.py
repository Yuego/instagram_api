from .base_response import Response

__all__ = ['VerifySMSCodeResponse']


class VerifySMSCodeResponse(Response):
    JSON_PROPERTY_MAP = {
        'verified': bool,
        'phone_number': str,
    }
