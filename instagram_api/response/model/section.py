from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .explore_item_info import ExploreItemInfo
from .layout_content import LayoutContent

__all__ = ['Section', 'SectionInterface']


class SectionInterface(ApiInterfaceBase):
    layout_type: str
    layout_content: LayoutContent
    feed_type: str
    explore_item_info: ExploreItemInfo


class Section(PropertyMapper, SectionInterface):
    pass
