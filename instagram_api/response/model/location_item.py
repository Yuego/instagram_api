from instagram_api.property_mapper import PropertyMapperBase

from .location import Location

__all__ = ['LocationItem']


class LocationItem(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'media_bundles': None,
        'subtitle': None,
        'location': Location,
        'title': None,
    }
