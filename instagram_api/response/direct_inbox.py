from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import DirectInbox, Megaphone, User

__all__ = ['DirectInboxResponse']


class DirectInboxResponseInterface(ApiResponseInterface):
    pending_requests_total: int
    seq_id: int
    pending_requests_users: [User]
    inbox: DirectInbox
    megaphone: Megaphone
    snapshot_at_ms: str


class DirectInboxResponse(ApiResponse, DirectInboxResponseInterface):
    pass
