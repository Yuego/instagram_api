from .base_response import Response

__all__ = ['DirectShareInboxResponse']


class DirectShareInboxResponse(Response):
    JSON_PROPERTY_MAP = {
        'shares': None,
        'max_id': str,
        'new_shares': None,
        'patches': None,
        'last_counted_at': None,
        'new_shares_info': None,
    }
