from .base_response import ApiResponse
from .model import User

__all__ = ['SwitchPersonalProfileResponse']


class SwitchPersonalProfileResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'users': [User],
    }
