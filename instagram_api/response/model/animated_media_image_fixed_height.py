from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['AnimatedMediaImageFixedHeight']


class AnimatedMediaImageFixedHeight(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'url': str,
        'width': str,
        'heigth': str,
        'size': str,
        'mp4': str,
        'mp4_size': str,
        'webp': str,
        'webp_size': str,
    }
