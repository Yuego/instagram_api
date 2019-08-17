from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .user import User

__all__ = ['InlineFollow', 'InlineFollowInterface']


class InlineFollowInterface(ApiInterfaceBase):
    user_info: User
    following: bool
    outgoing_request: bool


class InlineFollow(PropertyMapper, InlineFollowInterface):
    pass
