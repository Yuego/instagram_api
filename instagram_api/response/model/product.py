from instagram_api.property_mapper import PropertyMapperBase

from .product_image import ProductImage

__all__ = ['Product']


class Product(PropertyMapperBase):
    APPROVED = 'approved'
    PENDING = 'pending'
    REJECTED = 'rejected'

    JSON_PROPERTY_MAP = {
        'name': str,
        'price': str,
        'current_price': str,
        'full_price': str,
        'product_id': str,
        'has_viewer_saved': bool,
        'description': str,
        'main_image': ProductImage,
        'thumbnail_image': ProductImage,
        'product_images': [ProductImage],
        'external_url': str,
        'checkout_style': str,
        'review_status': str,
    }
