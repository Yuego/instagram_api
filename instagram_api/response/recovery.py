from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['RecoveryResponse']


class RecoveryResponseInterface(ApiResponseInterface):
    phone_number_valid: bool
    title: str
    body: str


class RecoveryResponse(ApiResponse, RecoveryResponseInterface):
    pass
