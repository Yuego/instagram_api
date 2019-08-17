from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType


__all__ = ['DirectExpiringSummary', 'DirectExpiringSummaryInterface']


class DirectExpiringSummaryInterface(ApiInterfaceBase):
    type: str
    timestamp: Timestamp
    count: int


class DirectExpiringSummary(PropertyMapper, DirectExpiringSummaryInterface):
    pass
