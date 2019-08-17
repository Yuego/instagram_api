from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .user import User

__all__ = ['Responder', 'ResponderInterface']


class ResponderInterface(ApiInterfaceBase):
    response: str
    has_shared_response: bool
    id: str
    user: User
    ts: int


class Responder(PropertyMapper, ResponderInterface):
    pass
