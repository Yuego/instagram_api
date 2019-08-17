from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .animated_media_image import AnimatedMediaImage

__all__ = ['AnimatedMedia', 'AnimatedMediaInterface']


class AnimatedMediaInterface(ApiInterfaceBase):
    id: int
    images: AnimatedMediaImage


class AnimatedMedia(PropertyMapper, AnimatedMediaInterface):
    pass
