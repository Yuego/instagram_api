from instagram_api.property_mapper import PropertyMapperBase

from .explore_item_info import ExploreItemInfo
from .section_media import SectionMedia
from .tabs_info import TabsInfo
from .tag import Tag

__all__ = ['LayoutContent']


class LayoutContent(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'related_style': str,
        'related': [Tag],
        'medias': [SectionMedia],
        'feed_type': str,
        'explore_item_info': ExploreItemInfo,
        'tabs_info': TabsInfo,
    }
