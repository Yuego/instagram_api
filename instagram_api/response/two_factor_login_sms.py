from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import TwoFactorInfo

__all__ = ['TwoFactorLoginSMSResponse']


class TwoFactorLoginSMSResponseInterface(ApiResponseInterface):
    two_factor_required: bool
    two_factor_info: TwoFactorInfo


class TwoFactorLoginSMSResponse(ApiResponse, TwoFactorLoginSMSResponseInterface):
    pass
