from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['MegaphoneLogResponse']


class MegaphoneLogResponseInterface(ApiResponseInterface):
    success: AnyType


class MegaphoneLogResponse(ApiResponse, MegaphoneLogResponseInterface):
    pass
