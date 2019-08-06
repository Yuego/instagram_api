from .base_response import Response
from .model import StaticStickers

__all__ = ['StickerAssetsResponse']


class StickerAssetsResponse(Response):
    JSON_PROPERTY_MAP = {
        'version': None,
        'static_stickers': [StaticStickers],
    }
