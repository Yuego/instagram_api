from .base_response import Response

__all__ = ['ProfileNoticeResponse']


class ProfileNoticeResponse(Response):
    JSON_PROPERTY_MAP = {
        'has_change_password_megaphone': bool,
    }
