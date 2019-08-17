from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .aymf_item import AymfItem

__all__ = ['Aymf', 'AymfInterface']


class AymfInterface(ApiInterfaceBase):
    items: [AymfItem]
    more_available: bool


class Aymf(PropertyMapper, AymfInterface):
    pass
