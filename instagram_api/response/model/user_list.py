from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .user import User

__all__ = ['UserList', 'UserListInterface']


class UserListInterface(ApiInterfaceBase):
    position: int
    user: User


class UserList(PropertyMapper, UserListInterface):
    pass
