from instagram_api.property_mapper import PropertyMapperBase

from .stickers import Stickers

__all__ = ['StaticStickers']


class StaticStickers(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'include_in_recent': None,
        'id': int,
        'stickers': [Stickers],
    }
