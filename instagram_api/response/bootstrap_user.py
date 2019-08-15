from .base_response import ApiResponse
from .model import Surface, User

__all__ = ['BootstrapUserResponse']


class BootstrapUserResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'surfaces': [Surface],
        'users': [User],
    }
