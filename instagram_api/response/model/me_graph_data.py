from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .catalog_data import CatalogData

__all__ = ['MeGraphData', 'MeGraphDataInterface']


class MeGraphDataInterface(ApiInterfaceBase):
    taggable_catalogs: CatalogData
    id: int


class MeGraphData(PropertyMapper, MeGraphDataInterface):
    pass
