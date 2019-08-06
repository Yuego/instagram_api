from .base_response import Response
from .model import DirectInbox, Megaphone, User

__all__ = ['DirectInboxResponse']


class DirectInboxResponse(Response):
    JSON_PROPERTY_MAP = {
        'pending_requests_total': int,
        'seq_id': int,
        'pending_requests_users': [User],
        'inbox': DirectInbox,
        'megaphone': Megaphone,
        'snapshot_at_ms': str,
    }
