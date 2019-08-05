from instagram_api.property_mapper import PropertyMapperBase

from .image_versions2 import ImageVersions2

__all__ = ['ProductImage']


class ProductImage(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'image_versions2': ImageVersions2,
    }
