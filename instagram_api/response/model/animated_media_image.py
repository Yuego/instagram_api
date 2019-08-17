from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .animated_media_image_fixed_height import AnimatedMediaImageFixedHeight

__all__ = ['AnimatedMediaImage', 'AnimatedMediaImageInterface']


class AnimatedMediaImageInterface(ApiInterfaceBase):
    fixed_height: AnimatedMediaImageFixedHeight


class AnimatedMediaImage(PropertyMapper, AnimatedMediaImageInterface):
    pass
