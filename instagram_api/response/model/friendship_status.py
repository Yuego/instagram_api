from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['FriendshipStatus', 'FriendshipStatusInterface']


class FriendshipStatusInterface(ApiInterfaceBase):
    following: bool
    followed_by: bool
    incoming_request: bool
    outgoing_request: bool
    is_private: bool
    is_blocking_reel: bool
    is_muting_reel: bool
    blocking: bool
    muting: bool
    is_bestie: bool
    is_restricted: bool


class FriendshipStatus(PropertyMapper, FriendshipStatusInterface):
    pass
