from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['Stickers']


class Stickers(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'id': int,
        'tray_image_width_ratio': None,
        'image_height': None,
        'image_width_ratio': None,
        'type': None,
        'image_width': None,
        'name': None,
        'image_url': str,
    }
