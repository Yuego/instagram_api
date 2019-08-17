from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['PresenceStatusResponse']


class PresenceStatusResponseInterface(ApiResponseInterface):
    disabled: bool
    thread_presence_disabled: bool


class PresenceStatusResponse(ApiResponse, PresenceStatusResponseInterface):
    pass
