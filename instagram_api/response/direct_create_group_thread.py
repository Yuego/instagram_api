from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import DirectThreadItem, User

__all__ = ['DirectCreateGroupThreadResponse']


class DirectCreateGroupThreadResponseInterface(ApiResponseInterface):
    thread_id: int
    users: [User]
    left_users: [User]
    items: [DirectThreadItem]
    last_activity_at: AnyType
    muted: AnyType
    named: AnyType
    canonical: AnyType
    pending: AnyType
    thread_type: AnyType
    viewer_id: str
    thread_title: AnyType
    inviter: User
    has_older: bool
    has_newer: bool
    last_seen_at: AnyType
    is_pin: AnyType


class DirectCreateGroupThreadResponse(ApiResponse, DirectCreateGroupThreadResponseInterface):
    pass
