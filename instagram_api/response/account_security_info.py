from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['AccountSecurityInfoResponse']


class AccountSecurityInfoResponseInterface(ApiResponseInterface):
    backup_codes: AnyType
    is_phone_confirmed: AnyType
    country_code: int
    phone_number: str
    is_two_factor_enabled: AnyType
    national_number: int


class AccountSecurityInfoResponse(ApiResponse, AccountSecurityInfoResponseInterface):
    pass
