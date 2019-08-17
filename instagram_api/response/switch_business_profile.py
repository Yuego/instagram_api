from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['SwitchBusinessProfileResponse']


class SwitchBusinessProfileResponseInterface(ApiResponseInterface):
    social_context: AnyType


class SwitchBusinessProfileResponse(ApiResponse, SwitchBusinessProfileResponseInterface):
    pass
