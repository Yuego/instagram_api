from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .user import User

__all__ = ['TopLive', 'TopLiveInterface']


class TopLiveInterface(ApiInterfaceBase):
    broadcast_owners: [User]
    ranked_position: AnyType


class TopLive(PropertyMapper, TopLiveInterface):
    pass
