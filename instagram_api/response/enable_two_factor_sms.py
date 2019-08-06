from .base_response import Response

__all__ = ['EnableTwoFactorSMSResponse']


class EnableTwoFactorSMSResponse(Response):
    JSON_PROPERTY_MAP = {
        'backup_codes': None,
    }
