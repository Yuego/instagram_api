from .base_response import ApiResponse
from .model import PhoneVerificationSettings

__all__ = ['SendSMSCodeResponse']


class SendSMSCodeResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'phone_number_valid': bool,
        'phone_verification_settings': PhoneVerificationSettings,
    }
