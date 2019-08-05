from instagram_api.property_mapper import PropertyMapperBase

from .explore_item_info import ExploreItemInfo
from .layout_content import LayoutContent

__all__ = ['Section']


class Section(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'layout_type': str,
        'layout_content': LayoutContent,
        'feed_type': str,
        'explore_item_info': ExploreItemInfo,
    }
