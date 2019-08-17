from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import LocationItem

__all__ = ['FBLocationResponse']


class FBLocationResponseInterface(ApiResponseInterface):
    has_more: bool
    items: [LocationItem]
    rank_token: str


class FBLocationResponse(ApiResponse, FBLocationResponseInterface):
    pass
