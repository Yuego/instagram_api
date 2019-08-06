from .model import User

from .base_response import Response

__all__ = ['AccountCreateResponse']


class AccountCreateResponse(Response):
    JSON_PROPERTY_MAP = {
        'account_created': None,
        'created_user': User,
    }
