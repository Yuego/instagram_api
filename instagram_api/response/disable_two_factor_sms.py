from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['DisableTwoFactorSMSResponse']


class DisableTwoFactorSMSResponseInterface(ApiResponseInterface):
    pass


class DisableTwoFactorSMSResponse(ApiResponse, DisableTwoFactorSMSResponseInterface):
    pass
