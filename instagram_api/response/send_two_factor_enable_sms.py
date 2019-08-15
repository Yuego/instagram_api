from .base_response import ApiResponse
from .model import PhoneVerificationSettings

__all__ = ['SendTwoFactorEnableSMSResponse']


class SendTwoFactorEnableSMSResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'phone_verification_settings': PhoneVerificationSettings,
        'obfuscated_phone_number': None,
    }
