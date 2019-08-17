from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['MediaSeenResponse']


class MediaSeenResponseInterface(ApiResponseInterface):
    pass


class MediaSeenResponse(ApiResponse, MediaSeenResponseInterface):
    pass
