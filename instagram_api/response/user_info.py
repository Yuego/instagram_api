from .base_response import Response
from .model import User

__all__ = ['UserInfoResponse']


class UserInfoResponse(Response):
    JSON_PROPERTY_MAP = {
        'megaphone': None,
        'user': User,
    }
