from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['Placeholder', 'PlaceholderInterface']


class PlaceholderInterface(ApiInterfaceBase):
    is_linked: bool
    title: str
    message: str


class Placeholder(PropertyMapper, PlaceholderInterface):
    pass
