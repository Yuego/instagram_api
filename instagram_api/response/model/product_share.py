from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .item import Item
from .product import Product

__all__ = ['ProductShare', 'ProductShareInterface']


class ProductShareInterface(ApiInterfaceBase):
    media: Item
    text: str
    product: Product


class ProductShare(PropertyMapper, ProductShareInterface):
    pass
