from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .user import User

__all__ = ['Voter', 'VoterInterface']


class VoterInterface(ApiInterfaceBase):
    user: User
    vote: int


class Voter(PropertyMapper, VoterInterface):
    pass
