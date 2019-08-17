from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .direct_thread import DirectThread
from .user import User

__all__ = ['DirectRankedRecipient', 'DirectRankedRecipientInterface']


class DirectRankedRecipientInterface(ApiInterfaceBase):
    thread: DirectThread
    user: User


class DirectRankedRecipient(PropertyMapper, DirectRankedRecipientInterface):
    pass
