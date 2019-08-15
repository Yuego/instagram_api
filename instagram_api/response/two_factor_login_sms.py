from .base_response import ApiResponse
from .model import TwoFactorInfo

__all__ = ['TwoFactorLoginSMSResponse']


class TwoFactorLoginSMSResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'two_factor_required': bool,
        'two_factor_info': TwoFactorInfo,
    }
