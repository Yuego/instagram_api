from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .item import Item

__all__ = ['Groups', 'GroupsInterface']


class GroupsInterface(ApiInterfaceBase):
    type: AnyType
    items: [Item]


class Groups(PropertyMapper, GroupsInterface):
    pass
