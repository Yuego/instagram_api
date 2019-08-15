from .model import User

from .base_response import ApiResponse

__all__ = ['AccountCreateResponse']


class AccountCreateResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'account_created': None,
        'created_user': User,
    }
