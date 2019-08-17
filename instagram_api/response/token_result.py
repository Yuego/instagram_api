from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import Token

__all__ = ['TokenResultResponse']


class TokenResultResponseInterface(ApiResponseInterface):
    token: Token


class TokenResultResponse(ApiResponse, TokenResultResponseInterface):
    pass
