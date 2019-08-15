from .base_response import ApiResponse
from .model import DirectRankedRecipient

__all__ = ['DirectRankedRecipientsResponse']


class DirectRankedRecipientsResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'expires': None,
        'ranked_recipients': [DirectRankedRecipient],
        'filtered': None,
        'request_id': str,
        'rank_token': str,
    }
