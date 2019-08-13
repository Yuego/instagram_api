from instagram_api.property_mapper import PropertyMapperBase

from .catalog_data import CatalogData
from .me_graph_data import MeGraphData
from .shadow_instagram_user import ShadowInstagramUser

__all__ = ['GraphData']


class GraphData(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        '__typename': str,
        'name': str,
        'user': ShadowInstagramUser,
        'error': None,
        'catalog_items': CatalogData,
        'me': MeGraphData,
    }
