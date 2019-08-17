from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['StartLiveResponse']


class StartLiveResponseInterface(ApiResponseInterface):
    media_id: int


class StartLiveResponse(ApiResponse, StartLiveResponseInterface):
    pass
