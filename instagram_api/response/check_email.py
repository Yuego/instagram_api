from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['CheckEmailResponse']


class CheckEmailResponseInterface(ApiResponseInterface):
    valid: AnyType
    available: AnyType
    confirmed: AnyType
    username_suggestions: [str]
    error_type: AnyType


class CheckEmailResponse(ApiResponse, CheckEmailResponseInterface):
    pass
