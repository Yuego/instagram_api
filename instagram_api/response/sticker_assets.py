from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import StaticStickers

__all__ = ['StickerAssetsResponse']


class StickerAssetsResponseInterface(ApiResponseInterface):
    version: AnyType
    static_stickers: [StaticStickers]


class StickerAssetsResponse(ApiResponse, StickerAssetsResponseInterface):
    pass
