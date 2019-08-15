from .base_response import ApiResponse
from .model import Product, User

__all__ = ['OnTagProductResponse']


class OnTagProductResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'product_item': Product,
        'merchant': User,
        'other_product_items': [Product],
    }
