from instagram_api.property_mapper import PropertyMapperBase

from .in_ import In

__all__ = ['ProductTags']


class ProductTags(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'in': [In],
    }
