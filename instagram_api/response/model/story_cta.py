from instagram_api.property_mapper import PropertyMapperBase

from .android_links import AndroidLinks

__all__ = ['StoryCta']


class StoryCta(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'links': [AndroidLinks],
        'felix_deep_link': str,
    }
