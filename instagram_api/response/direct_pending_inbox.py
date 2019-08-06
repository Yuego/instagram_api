from .base_response import Response
from .model import DirectInbox

__all__ = ['DirectPendingInboxResponse']


class DirectPendingInboxResponse(Response):
    JSON_PROPERTY_MAP = {
        'seq_id': int,
        'pending_requests_total': int,
        'inbox': DirectInbox,
    }
