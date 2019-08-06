from .base_response import Response
from .model import TwoFactorInfo

__all__ = ['TwoFactorLoginSMSResponse']


class TwoFactorLoginSMSResponse(Response):
    JSON_PROPERTY_MAP = {
        'two_factor_required': bool,
        'two_factor_info': TwoFactorInfo,
    }
