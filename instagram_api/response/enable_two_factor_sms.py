from .base_response import ApiResponse

__all__ = ['EnableTwoFactorSMSResponse']


class EnableTwoFactorSMSResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'backup_codes': None,
    }
