from .base_response import Response
from .model import DirectRankedRecipient

__all__ = ['DirectRankedRecipientsResponse']


class DirectRankedRecipientsResponse(Response):
    JSON_PROPERTY_MAP = {
        'expires': None,
        'ranked_recipients': [DirectRankedRecipient],
        'filtered': None,
        'request_id': str,
        'rank_token': str,
    }
