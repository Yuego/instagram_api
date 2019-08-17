from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import User

__all__ = ['SwitchPersonalProfileResponse']


class SwitchPersonalProfileResponseInterface(ApiResponseInterface):
    users: [User]


class SwitchPersonalProfileResponse(ApiResponse, SwitchPersonalProfileResponseInterface):
    pass
