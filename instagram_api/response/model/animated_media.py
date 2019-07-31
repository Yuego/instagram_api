from instagram_api.property_mapper import PropertyMapperBase

from .animated_media_image import AnimatedMediaImage

__all__ = ['AnimatedMediaImage']


class AnimatedMedia(PropertyMapperBase):

    JSON_PROPERTY_MAP = {
        'id': str,
        'images': AnimatedMediaImage,
    }
