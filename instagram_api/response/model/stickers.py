from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['Stickers', 'StickersInterface']


class StickersInterface(ApiInterfaceBase):
    id: int
    tray_image_width_ratio: AnyType
    image_height: AnyType
    image_width_ratio: AnyType
    type: AnyType
    image_width: AnyType
    name: AnyType
    image_url: str


class Stickers(PropertyMapper, StickersInterface):
    pass
