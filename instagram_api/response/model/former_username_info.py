from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['FormerUsernameInfo', 'FormerUsernameInfoInterface']


class FormerUsernameInfoInterface(ApiInterfaceBase):
    has_former_usernames: bool


class FormerUsernameInfo(PropertyMapper, FormerUsernameInfoInterface):
    pass
