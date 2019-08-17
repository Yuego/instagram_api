from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['SaveAndUnsaveMediaResponse']


class SaveAndUnsaveMediaResponseInterface(ApiResponseInterface):
    pass


class SaveAndUnsaveMediaResponse(ApiResponse, SaveAndUnsaveMediaResponseInterface):
    pass
