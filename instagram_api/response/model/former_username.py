from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['FormerUsername', 'FormerUsernameInterface']


class FormerUsernameInterface(ApiInterfaceBase):
    former_username: str
    change_timestamp: Timestamp


class FormerUsername(PropertyMapper, FormerUsernameInterface):
    pass
