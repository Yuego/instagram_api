from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import User

__all__ = ['CommentLikersResponse']


class CommentLikersResponseInterface(ApiResponseInterface):
    users: [User]


class CommentLikersResponse(ApiResponse, CommentLikersResponseInterface):
    pass
