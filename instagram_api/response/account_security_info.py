from .base_response import ApiResponse

__all__ = ['AccountSecurityInfoResponse']


class AccountSecurityInfoResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'backup_codes': None,
        'is_phone_confirmed': None,
        'country_code': int,
        'phone_number': str,
        'is_two_factor_enabled': None,
        'national_number': int,
    }
