from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .item import Item

__all__ = ['Ad4ad', 'Ad4adInterface']


class Ad4adInterface(ApiInterfaceBase):
    type: AnyType
    title: str
    media: Item
    footer: AnyType
    id: str
    tracking_token: str


class Ad4ad(PropertyMapper, Ad4adInterface):
    pass
