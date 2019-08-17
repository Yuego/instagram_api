from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['Image', 'ImageInterface']


class ImageInterface(ApiInterfaceBase):
    uri: str
    width: int
    height: int


class Image(PropertyMapper, ImageInterface):
    pass
