from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['PhoneVerificationSettings']


class PhoneVerificationSettings(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'resend_sms_delay_sec': int,
        'max_sms_count': int,
        'robocall_count_down_time_sec': int,
        'robocall_after_max_sms': bool,
    }
