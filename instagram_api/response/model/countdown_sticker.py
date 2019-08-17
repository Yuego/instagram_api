from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['CountdownSticker', 'CountdownStickerInterface']


class CountdownStickerInterface(ApiInterfaceBase):
    countdown_id: int
    end_ts: str
    text: str
    text_color: str
    start_background_color: str
    end_background_color: str
    digit_color: str
    digit_card_color: str
    following_enabled: bool
    is_owner: bool
    attribution: AnyType
    viewer_is_following: bool


class CountdownSticker(PropertyMapper, CountdownStickerInterface):
    pass
