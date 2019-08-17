from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import Location

__all__ = ['LocationResponse']


class LocationResponseInterface(ApiResponseInterface):
    venues: [Location]
    request_id: str


class LocationResponse(ApiResponse, LocationResponseInterface):
    pass
