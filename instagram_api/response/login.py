from .base_response import ApiResponse
from .model import Challenge, PhoneVerificationSettings, TwoFactorInfo, User

__all__ = ['LoginResponse']


class LoginResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'username': str,
        'has_anonymous_profile_picture': bool,
        'profile_pic_url': str,
        'profile_pic_id': str,
        'full_name': str,
        'pk': str,
        'is_private': bool,
        'is_verified': bool,
        'allowed_commenter_type': str,
        'reel_auto_archive': str,
        'allow_contacts_sync': bool,
        'phone_number': str,
        'country_code': int,
        'national_number': int,
        'error_title': None,  # On wrong pass.
        'error_type': None,  # On wrong pass.
        'buttons': None,  # On wrong pass.
        'invalid_credentials': None,  # On wrong pass.
        'logged_in_user': User,
        'two_factor_required': None,
        'phone_verification_settings': PhoneVerificationSettings,
        'two_factor_info': TwoFactorInfo,
        'checkpoint_url': str,
        'lock': None,
        'help_url': str,
        'challenge': Challenge,
    }
