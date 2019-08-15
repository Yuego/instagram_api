from .base_response import ApiResponse
from .model import StaticStickers

__all__ = ['StickerAssetsResponse']


class StickerAssetsResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'version': None,
        'static_stickers': [StaticStickers],
    }
