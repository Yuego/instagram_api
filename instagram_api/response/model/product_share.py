from instagram_api.property_mapper import PropertyMapperBase

from .item import Item
from .product import Product

__all__ = ['ProductShare']


class ProductShare(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'media': Item,
        'text': str,
        'product': Product,
    }
