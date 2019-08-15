from .base_response import ApiResponse

__all__ = ['DirectRecentRecipientsResponse']


class DirectRecentRecipientsResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'expiration_interval': None,
        'recent_recipients': None,
    }
