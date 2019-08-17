from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import User

__all__ = ['UsersLookupResponse']


class UsersLookupResponseInterface(ApiResponseInterface):
    user: User
    email_sent: bool
    has_valid_phone: bool
    can_email_reset: bool
    can_sms_reset: bool
    user_id: str
    lookup_source: str
    email: str
    phone_number: str
    corrected_input: str


class UsersLookupResponse(ApiResponse, UsersLookupResponseInterface):
    pass
