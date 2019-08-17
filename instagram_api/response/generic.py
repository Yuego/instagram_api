from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['GenericResponse']


class GenericResponseInterface(ApiResponseInterface):
    pass


class GenericResponse(ApiResponse, GenericResponseInterface):
    pass
