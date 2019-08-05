from instagram_api.property_mapper import PropertyMapperBase

from .location import Location

__all__ = ['Owner']


class Owner(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'type': None,
        'pk': int,
        'name': str,
        'profile_pic_url': str,
        'profile_pic_username': str,
        'short_name': str,
        'lat': float,
        'lng': float,
        'location_dict': Location,
    }
