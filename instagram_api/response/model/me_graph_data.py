from instagram_api.property_mapper import PropertyMapperBase

from .catalog_data import CatalogData

__all__ = ['MeGraphData']


class MeGraphData(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'taggable_catalogs': CatalogData,
        'id': int,
    }
