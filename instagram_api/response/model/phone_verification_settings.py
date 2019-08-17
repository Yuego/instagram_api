from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['PhoneVerificationSettings', 'PhoneVerificationSettingsInterface']


class PhoneVerificationSettingsInterface(ApiInterfaceBase):
    resend_sms_delay_sec: int
    max_sms_count: int
    robocall_count_down_time_sec: int
    robocall_after_max_sms: bool


class PhoneVerificationSettings(PropertyMapper, PhoneVerificationSettingsInterface):
    pass
