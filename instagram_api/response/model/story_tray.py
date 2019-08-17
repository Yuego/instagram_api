from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType, Lazy

from .cover_media import CoverMedia
from .dismiss_card import DismissCard
from .location import Location
from .owner import Owner
from .user import User

__all__ = ['StoryTray', 'StoryTrayInterface']


class StoryTrayInterface(ApiInterfaceBase):
    id: int
    items: Lazy.model__item__Item
    user: User
    can_reply: AnyType
    expiring_at: Timestamp
    seen_ranked_position: str
    seen: str
    latest_reel_media: str
    ranked_position: str
    is_nux: AnyType
    show_nux_tooltip: AnyType
    muted: AnyType
    prefetch_count: int
    location: Location
    source_token: AnyType
    owner: Owner
    nux_id: int
    dismiss_card: DismissCard
    can_reshare: AnyType
    has_besties_media: bool
    reel_type: str
    unique_integer_reel_id: int
    cover_media: CoverMedia
    title: str
    media_count: int


class StoryTray(PropertyMapper, StoryTrayInterface):
    pass
