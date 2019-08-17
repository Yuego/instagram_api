from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .user import User

__all__ = ['CloseFriends', 'CloseFriendsInterface']


class CloseFriendsInterface(ApiInterfaceBase):
    sections: AnyType
    users: [User]
    big_list: AnyType
    page_size: AnyType


class CloseFriends(PropertyMapper, CloseFriendsInterface):
    pass
