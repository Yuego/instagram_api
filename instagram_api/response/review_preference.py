from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import User

__all__ = ['ReviewPreferenceResponse']


class ReviewPreferenceResponseInterface(ApiResponseInterface):
    user: User


class ReviewPreferenceResponse(ApiResponse, ReviewPreferenceResponseInterface):
    pass
