from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['BlockedMediaResponse']


class BlockedMediaResponseInterface(ApiResponseInterface):
    media_ids: AnyType


class BlockedMediaResponse(ApiResponse, BlockedMediaResponseInterface):
    pass
