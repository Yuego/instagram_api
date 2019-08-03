from instagram_api.property_mapper import PropertyMapperBase

from .catalog_node import CatalogNode

__all__ = ['CatalogEdge']


class CatalogEdge(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'node': CatalogNode,
    }
