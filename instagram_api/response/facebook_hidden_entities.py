from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import HiddenEntities

__all__ = ['FacebookHiddenEntitiesResponse']


class FacebookHiddenEntitiesResponseInterface(ApiResponseInterface):
    recent: HiddenEntities


class FacebookHiddenEntitiesResponse(ApiResponse, FacebookHiddenEntitiesResponseInterface):
    pass
