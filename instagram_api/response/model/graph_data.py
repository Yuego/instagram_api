from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .catalog_data import CatalogData
from .me_graph_data import MeGraphData
from .shadow_instagram_user import ShadowInstagramUser

__all__ = ['GraphData', 'GraphDataInterface']


class GraphDataInterface(ApiInterfaceBase):
    __typename: str
    name: str
    user: ShadowInstagramUser
    error: AnyType
    catalog_items: CatalogData
    me: MeGraphData


class GraphData(PropertyMapper, GraphDataInterface):
    pass
