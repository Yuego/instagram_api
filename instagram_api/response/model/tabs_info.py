from instagram_api.property_mapper import PropertyMapperBase

from .tab import Tab

__all__ = ['TabsInfo']


class TabsInfo(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'tabs': [Tab],
        'selected': str,
    }
