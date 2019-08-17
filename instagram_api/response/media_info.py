from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import Item

__all__ = ['MediaInfoResponse']


class MediaInfoResponseInterface(ApiResponseInterface):
    auto_load_more_enabled: AnyType
    num_results: int
    more_available: bool
    items: [Item]


class MediaInfoResponse(ApiResponse, MediaInfoResponseInterface):
    pass
