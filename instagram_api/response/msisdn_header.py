from .base_response import Response

__all__ = ['MsisdnHeaderResponse']


class MsisdnHeaderResponse(Response):
    JSON_PROPERTY_MAP = {
        'phone_number': str,
        'url': str,
        'remaining_ttl_seconds': int,
        'ttl': int,
    }
