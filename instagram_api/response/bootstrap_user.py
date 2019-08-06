from .base_response import Response
from .model import Surface, User

__all__ = ['BootstrapUserResponse']


class BootstrapUserResponse(Response):
    JSON_PROPERTY_MAP = {
        'surfaces': [Surface],
        'users': [User],
    }
