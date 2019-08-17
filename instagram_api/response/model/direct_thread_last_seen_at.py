from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType


__all__ = ['DirectThreadLastSeenAt', 'DirectThreadLastSeenAtInterface']


class DirectThreadLastSeenAtInterface(ApiInterfaceBase):
    item_id: int
    timestamp: Timestamp


class DirectThreadLastSeenAt(PropertyMapper, DirectThreadLastSeenAtInterface):
    pass
