from .base_response import ApiResponse

__all__ = ['ProfileNoticeResponse']


class ProfileNoticeResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'has_change_password_megaphone': bool,
    }
