from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType
from .page_info import PageInfo
from .catalog_edge import CatalogEdge

__all__ = ['CatalogData', 'CatalogDataInterface']


class CatalogDataInterface(ApiInterfaceBase):
    page_info: PageInfo
    edges: [CatalogEdge]


class CatalogData(PropertyMapper, CatalogDataInterface):
    pass
