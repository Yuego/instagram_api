from .base_response import Response
from .model import Product, User

__all__ = ['OnTagProductResponse']


class OnTagProductResponse(Response):
    JSON_PROPERTY_MAP = {
        'product_item': Product,
        'merchant': User,
        'other_product_items': [Product],
    }
