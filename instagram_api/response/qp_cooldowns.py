from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import QPSurface, Slot

__all__ = ['QPCooldownsResponse']


class QPCooldownsResponseInterface(ApiResponseInterface):
    global__: int  # TODO: разобраться со служебными именами
    default: int
    surfaces: [QPSurface]
    slots: [Slot]


class QPCooldownsResponse(ApiResponse, QPCooldownsResponseInterface):
    pass
