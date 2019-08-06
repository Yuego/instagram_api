from .base_response import Response
from .model import PhoneVerificationSettings

__all__ = ['SendSMSCodeResponse']


class SendSMSCodeResponse(Response):
    JSON_PROPERTY_MAP = {
        'phone_number_valid': bool,
        'phone_verification_settings': PhoneVerificationSettings,
    }
