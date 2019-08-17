from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .image_versions2 import ImageVersions2

__all__ = ['ProductImage', 'ProductImageInterface']


class ProductImageInterface(ApiInterfaceBase):
    image_versions2: ImageVersions2


class ProductImage(PropertyMapper, ProductImageInterface):
    pass
