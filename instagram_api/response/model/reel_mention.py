from ..mapper import PropertyMapper
from .common.sticker import StickerInterface
from .user import User

__all__ = ['ReelMention', 'ReelMentionInterface']


class ReelMentionInterface(StickerInterface):
    user: User
    is_hidden: int


class ReelMention(PropertyMapper, ReelMentionInterface):
    pass
