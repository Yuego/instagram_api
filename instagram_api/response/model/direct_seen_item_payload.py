from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType


__all__ = ['DirectSeenItemPayload', 'DirectSeenItemPayloadInterface']


class DirectSeenItemPayloadInterface(ApiInterfaceBase):
    count: int
    timestamp: Timestamp


class DirectSeenItemPayload(PropertyMapper, DirectSeenItemPayloadInterface):
    pass
