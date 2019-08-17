from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import FormerUsername

__all__ = ['FormerUsernamesResponse']


class FormerUsernamesResponseInterface(ApiResponseInterface):
    former_usernames: [FormerUsername]


class FormerUsernamesResponse(ApiResponse, FormerUsernamesResponseInterface):
    pass
