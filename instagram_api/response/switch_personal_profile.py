from .base_response import Response
from .model import User

__all__ = ['SwitchPersonalProfileResponse']


class SwitchPersonalProfileResponse(Response):
    JSON_PROPERTY_MAP = {
        'users': [User],
    }
