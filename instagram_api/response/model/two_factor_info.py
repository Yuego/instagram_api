from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .phone_verification_settings import PhoneVerificationSettings

__all__ = ['TwoFactorInfo', 'TwoFactorInfoInterface']


class TwoFactorInfoInterface(ApiInterfaceBase):
    username: str
    two_factor_identifier: str
    phone_verification_settings: PhoneVerificationSettings
    obfuscated_phone_number: str
    sms_two_factor_on: bool
    totp_two_factor_on: bool
    show_messenger_code_option: bool
    show_new_login_screen: bool
    show_trusted_device_option: bool


class TwoFactorInfo(PropertyMapper, TwoFactorInfoInterface):
    pass
