from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .in_ import In

__all__ = ['ProductTags', 'ProductTagsInterface']


# TODO: решить проблему со служебными словами
class ProductTagsInterface(ApiInterfaceBase):
    in__: [In]


class ProductTags(PropertyMapper, ProductTagsInterface):
    pass

