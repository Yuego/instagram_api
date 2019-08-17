from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .catalog_node import CatalogNode

__all__ = ['CatalogEdge', 'CatalogEdgeInterface']


class CatalogEdgeInterface(ApiInterfaceBase):
    node: CatalogNode


class CatalogEdge(PropertyMapper, CatalogEdgeInterface):
    pass
