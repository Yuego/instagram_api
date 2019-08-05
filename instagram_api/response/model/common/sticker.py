from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['Sticker']


class Sticker(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'x': float,
        'y': float,
        'z': float,
        'width': float,
        'height': float,
        'rotation': float,
        'is_pinned': int,
    }
