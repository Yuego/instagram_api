from instagram_api.property_mapper import PropertyMapperBase

from .viewer import Viewer

__all__ = ['QPViewerData']


class QPViewerData(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'viewer': Viewer,
    }
