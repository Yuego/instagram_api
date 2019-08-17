from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['ValidateURLResponse']


class ValidateURLResponseInterface(ApiResponseInterface):
    pass


class ValidateURLResponse(ApiResponse, ValidateURLResponseInterface):
    pass
