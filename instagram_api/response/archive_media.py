from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['ArchiveMediaResponse']


class ArchiveMediaResponseInterface(ApiResponseInterface):
    pass


class ArchiveMediaResponse(ApiResponse, ArchiveMediaResponseInterface):
    pass
