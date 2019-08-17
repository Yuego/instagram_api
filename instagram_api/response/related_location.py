from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import Location

__all__ = ['RelatedLocationResponse']


class RelatedLocationResponseInterface(ApiResponseInterface):
    related: [Location]


class RelatedLocationResponse(ApiResponse, RelatedLocationResponseInterface):
    pass
