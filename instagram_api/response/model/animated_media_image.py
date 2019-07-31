from instagram_api.property_mapper import PropertyMapperBase

from .animated_media_image_fixed_height import AnimatedMediaImageFixedHeight

__all__ = ['AnimatedMediaImage']


class AnimatedMediaImage(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'fixed_height': AnimatedMediaImageFixedHeight,
    }
