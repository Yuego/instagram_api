from .base_response import Response
from .model import PhoneVerificationSettings

__all__ = ['SendTwoFactorEnableSMSResponse']


class SendTwoFactorEnableSMSResponse(Response):
    JSON_PROPERTY_MAP = {
        'phone_verification_settings': PhoneVerificationSettings,
        'obfuscated_phone_number': None,
    }
