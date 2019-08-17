from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['VerifySMSCodeResponse']


class VerifySMSCodeResponseInterface(ApiResponseInterface):
    verified: bool
    phone_number: str


class VerifySMSCodeResponse(ApiResponse, VerifySMSCodeResponseInterface):
    pass
