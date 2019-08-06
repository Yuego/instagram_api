from instagram_api.property_mapper import PropertyMapperBase
from instagram_api.property_mapper.types import timestamp, LazyType

from .cover_media import CoverMedia
from .dismiss_card import DismissCard
# from .item import Item
from .location import Location
from .owner import Owner
from .user import User

__all__ = ['StoryTray']


class StoryTray(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'id': int,
        'items': [LazyType('model.item.Item')],
        'user': User,
        'can_reply': None,
        'expiring_at': timestamp,
        'seen_ranked_position': str,
        'seen': str,
        'latest_reel_media': str,
        'ranked_position': str,
        'is_nux': None,
        'show_nux_tooltip': None,
        'muted': None,
        'prefetch_count': int,
        'location': Location,
        'source_token': None,
        'owner': Owner,
        'nux_id': int,
        'dismiss_card': DismissCard,
        'can_reshare': None,
        'has_besties_media': bool,
        'reel_type': str,
        'unique_integer_reel_id': int,
        'cover_media': CoverMedia,
        'title': str,
        'media_count': int,
    }
