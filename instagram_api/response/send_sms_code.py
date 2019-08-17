from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import PhoneVerificationSettings

__all__ = ['SendSMSCodeResponse']


class SendSMSCodeResponseInterface(ApiResponseInterface):
    phone_number_valid: bool
    phone_verification_settings: PhoneVerificationSettings


class SendSMSCodeResponse(ApiResponse, SendSMSCodeResponseInterface):
    pass
