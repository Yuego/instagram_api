from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType, Lazy

__all__ = ['ReelShare', 'ReelShareInterface']


class ReelShareInterface(ApiInterfaceBase):
    tray: Lazy.model__item__Item
    story_ranking_token: str
    broadcasts: AnyType
    sticker_version: int
    text: str
    type: str
    is_reel_persisted: bool
    reel_owner_id: int
    reel_type: str
    media: Lazy.model__item__Item
    mentioned_user_id: int


class ReelShare(PropertyMapper, ReelShareInterface):
    pass
