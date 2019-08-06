from .base_response import Response

__all__ = ['DirectRecentRecipientsResponse']


class DirectRecentRecipientsResponse(Response):
    JSON_PROPERTY_MAP = {
        'expiration_interval': None,
        'recent_recipients': None,
    }
