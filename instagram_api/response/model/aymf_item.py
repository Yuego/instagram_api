from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['AymfItem', 'AymfItemInterface']


class AymfItemInterface(ApiInterfaceBase):
    caption: str
    uuid: str


class AymfItem(PropertyMapper, AymfItemInterface):
    pass
