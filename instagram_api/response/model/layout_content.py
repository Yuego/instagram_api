from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .explore_item_info import ExploreItemInfo
from .section_media import SectionMedia
from .tabs_info import TabsInfo
from .tag import Tag

__all__ = ['LayoutContent', 'LayoutContentInterface']


class LayoutContentInterface(ApiInterfaceBase):
    related_style: str
    related: [Tag]
    medias: [SectionMedia]
    feed_type: str
    explore_item_info: ExploreItemInfo
    tabs_info: TabsInfo


class LayoutContent(PropertyMapper, LayoutContentInterface):
    pass
