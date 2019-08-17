from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['AnimatedMediaImageFixedHeight', 'AnimatedMediaImageFixedHeightInterface']


class AnimatedMediaImageFixedHeightInterface(ApiInterfaceBase):
    url: str
    width: str
    heigth: str
    size: str
    mp4: str
    mp4_size: str
    webp: str
    webp_size: str


class AnimatedMediaImageFixedHeight(PropertyMapper, AnimatedMediaImageFixedHeightInterface):
    pass
