from instagram_api.property_mapper import PropertyMapperBase

from .in_ import In

__all__ = ['UserTag']


class UserTag(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'in': [In],
        'photo_of_you': bool,
    }
