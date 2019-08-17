from .model import User

from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['AccountCreateResponse']


class AccountCreateResponseInterface(ApiResponseInterface):
    account_created: AnyType
    created_user: User


class AccountCreateResponse(ApiResponse, AccountCreateResponseInterface):
    pass
