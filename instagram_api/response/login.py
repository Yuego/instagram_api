from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import Challenge, PhoneVerificationSettings, TwoFactorInfo, User

__all__ = ['LoginResponse']


class LoginResponseInterface(ApiResponseInterface):
    username: str
    has_anonymous_profile_picture: bool
    profile_pic_url: str
    profile_pic_id: str
    full_name: str
    pk: int
    is_private: bool
    is_verified: bool
    allowed_commenter_type: str
    reel_auto_archive: str
    allow_contacts_sync: bool
    phone_number: str
    country_code: int
    national_number: int
    error_title: AnyType  # On wrong pass.
    error_type: AnyType  # On wrong pass.
    buttons: AnyType  # On wrong pass.
    invalid_credentials: AnyType  # On wrong pass.
    logged_in_user: User
    two_factor_required: AnyType
    phone_verification_settings: PhoneVerificationSettings
    two_factor_info: TwoFactorInfo
    checkpoint_url: str
    lock: AnyType
    help_url: str
    challenge: Challenge


class LoginResponse(ApiResponse, LoginResponseInterface):
    pass
