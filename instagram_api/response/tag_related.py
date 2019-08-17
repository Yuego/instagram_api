from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import Related

__all__ = ['TagRelatedResponse']


class TagRelatedResponseInterface(ApiResponseInterface):
    related: [Related]


class TagRelatedResponse(ApiResponse, TagRelatedResponseInterface):
    pass
