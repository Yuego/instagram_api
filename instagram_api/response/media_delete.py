from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['MediaDeleteResponse']


class MediaDeleteResponseInterface(ApiResponseInterface):
    did_delete: AnyType


class MediaDeleteResponse(ApiResponse, MediaDeleteResponseInterface):
    pass
