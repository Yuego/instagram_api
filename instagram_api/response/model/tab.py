from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['Tab', 'TabInterface']


class TabInterface(ApiInterfaceBase):
    type: str
    title: str


class Tab(PropertyMapper, TabInterface):
    pass
