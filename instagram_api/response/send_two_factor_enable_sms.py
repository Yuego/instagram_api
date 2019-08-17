from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import PhoneVerificationSettings

__all__ = ['SendTwoFactorEnableSMSResponse']


class SendTwoFactorEnableSMSResponseInterface(ApiResponseInterface):
    phone_verification_settings: PhoneVerificationSettings
    obfuscated_phone_number: AnyType


class SendTwoFactorEnableSMSResponse(ApiResponse, SendTwoFactorEnableSMSResponseInterface):
    pass
