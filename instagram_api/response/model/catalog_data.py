from instagram_api.property_mapper import PropertyMapperBase
from .page_info import PageInfo
from .catalog_edge import CatalogEdge

__all__ = ['CatalogData']


class CatalogData(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'page_info': PageInfo,
        'edges': [CatalogEdge],
    }
