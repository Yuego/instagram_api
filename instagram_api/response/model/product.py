from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .product_image import ProductImage

__all__ = ['Product', 'ProductInterface']


class ProductInterface(ApiInterfaceBase):
    APPROVED = 'approved'
    PENDING = 'pending'
    REJECTED = 'rejected'

    name: str
    price: str
    current_price: str
    full_price: str
    product_id: int
    has_viewer_saved: bool
    description: str
    main_image: ProductImage
    thumbnail_image: ProductImage
    product_images: [ProductImage]
    external_url: str
    checkout_style: str
    review_status: str


class Product(PropertyMapper, ProductInterface):
    pass
