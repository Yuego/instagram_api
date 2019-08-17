from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['Text', 'TextInterface']


class TextInterface(ApiInterfaceBase):
    text: str


class Text(PropertyMapper, TextInterface):
    pass
