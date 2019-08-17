from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['PermalinkResponse']


class PermalinkResponseInterface(ApiResponseInterface):
    permalink: str


class PermalinkResponse(ApiResponse, PermalinkResponseInterface):
    pass
