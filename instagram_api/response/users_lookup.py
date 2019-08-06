from .base_response import Response
from .model import User

__all__ = ['UsersLookupResponse']


class UsersLookupResponse(Response):
    JSON_PROPERTY_MAP = {
        'user': User,
        'email_sent': bool,
        'has_valid_phone': bool,
        'can_email_reset': bool,
        'can_sms_reset': bool,
        'user_id': str,
        'lookup_source': str,
        'email': str,
        'phone_number': str,
        'corrected_input': str,
    }
