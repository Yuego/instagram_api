from .base_response import ApiResponse
from .model import DirectInbox

__all__ = ['DirectPendingInboxResponse']


class DirectPendingInboxResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'seq_id': int,
        'pending_requests_total': int,
        'inbox': DirectInbox,
    }
