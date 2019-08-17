from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['EnableTwoFactorSMSResponse']


class EnableTwoFactorSMSResponseInterface(ApiResponseInterface):
    backup_codes: AnyType


class EnableTwoFactorSMSResponse(ApiResponse, EnableTwoFactorSMSResponseInterface):
    pass
