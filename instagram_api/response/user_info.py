from .base_response import ApiResponse
from .model import User

__all__ = ['UserInfoResponse']


class UserInfoResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'megaphone': None,
        'user': User,
    }
