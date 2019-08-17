from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['UnknownMessage', 'UnknownMessageInterface']


class UnknownMessageInterface(ApiInterfaceBase):
    key: str
    time: str


class UnknownMessage(PropertyMapper, UnknownMessageInterface):
    pass
