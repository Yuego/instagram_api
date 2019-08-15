from .base_response import ApiResponse

__all__ = ['MsisdnHeaderResponse']


class MsisdnHeaderResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'phone_number': str,
        'url': str,
        'remaining_ttl_seconds': int,
        'ttl': int,
    }
