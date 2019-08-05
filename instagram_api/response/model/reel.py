from instagram_api.property_mapper import PropertyMapperBase

from .broadcast import Broadcast
from .cover_media import CoverMedia
from .item import Item
from .location import Location
from .user import User

__all__ = ['Reel']


class Reel(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'id': int,
        'latest_reel_media': str,
        'seen': str,
        'can_reply': bool,
        'can_reshare': bool,
        'reel_type': str,
        'cover_media': CoverMedia,
        'user': User,
        'items': [Item],
        'ranked_position': str,
        'title': str,
        'seen_ranked_position': str,
        'expiring_at': str,
        'has_besties_media': bool,
        'location': Location,
        'prefetch_count': int,
        'broadcast': Broadcast,
    }
