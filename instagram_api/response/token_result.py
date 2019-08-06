from .base_response import Response
from .model import Token

__all__ = ['TokenResultResponse']


class TokenResultResponse(Response):
    JSON_PROPERTY_MAP = {
        'token': Token,
    }
