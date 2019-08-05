from .common.sticker import Sticker
from .user import User

__all__ = ['ReelMention']


class ReelMention(Sticker):
    JSON_PROPERTY_MAP = {
        'user': User,
        'is_hidden': int,
    }
