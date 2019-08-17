from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import DirectInbox

__all__ = ['DirectPendingInboxResponse']


class DirectPendingInboxResponseInterface(ApiResponseInterface):
    seq_id: int
    pending_requests_total: int
    inbox: DirectInbox


class DirectPendingInboxResponse(ApiResponse, DirectPendingInboxResponseInterface):
    pass
