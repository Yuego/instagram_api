from instagram_api.property_mapper import PropertyMapperBase

from .qp_viewer_data import QPViewerData

__all__ = ['QPData']


class QPData(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'surface': int,
        'data': QPViewerData,
    }
