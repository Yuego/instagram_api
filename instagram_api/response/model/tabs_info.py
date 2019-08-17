from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .tab import Tab

__all__ = ['TabsInfo', 'TabsInfoInterface']


class TabsInfoInterface(ApiInterfaceBase):
    tabs: [Tab]
    selected: str


class TabsInfo(PropertyMapper, TabsInfoInterface):
    pass
