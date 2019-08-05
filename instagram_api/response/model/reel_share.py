from instagram_api.property_mapper import PropertyMapperBase

from .item import Item

__all__ = ['ReelShare']


class ReelShare(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'tray': [Item],
        'story_ranking_token': str,
        'broadcasts': None,
        'sticker_version': int,
        'text': str,
        'type': str,
        'is_reel_persisted': bool,
        'reel_owner_id': str,
        'reel_type': str,
        'media': Item,
        'mentioned_user_id': str,
    }
