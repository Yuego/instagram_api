from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import Product, User

__all__ = ['OnTagProductResponse']


class OnTagProductResponseInterface(ApiResponseInterface):
    product_item: Product
    merchant: User
    other_product_items: [Product]


class OnTagProductResponse(ApiResponse, OnTagProductResponseInterface):
    pass
