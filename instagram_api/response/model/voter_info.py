from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .voter import Voter

__all__ = ['VoterInfo', 'VoterInfoInterface']


class VoterInfoInterface(ApiInterfaceBase):
    poll_id: int
    voters: [Voter]
    max_id: int
    more_available: bool


class VoterInfo(PropertyMapper, VoterInfoInterface):
    pass
