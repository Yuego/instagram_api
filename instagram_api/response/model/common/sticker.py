from ...mapper import PropertyMapper, ApiInterfaceBase

__all__ = ['Sticker', 'StickerInterface']


class StickerInterface(ApiInterfaceBase):
    x: float

    y: float

    z: float

    width: float

    height: float

    rotation: float

    is_pinned: int


class Sticker(PropertyMapper, StickerInterface):
    pass
