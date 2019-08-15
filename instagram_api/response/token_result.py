from .base_response import ApiResponse
from .model import Token

__all__ = ['TokenResultResponse']


class TokenResultResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'token': Token,
    }
