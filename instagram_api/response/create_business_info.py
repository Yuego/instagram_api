from .base_response import Response
from .model import User

__all__ = ['CreateBusinessInfoResponse']


class CreateBusinessInfoResponse(Response):
    JSON_PROPERTY_MAP = {
        'users': [User],
    }
