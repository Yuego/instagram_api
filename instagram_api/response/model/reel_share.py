from instagram_api.property_mapper import PropertyMapperBase
from instagram_api.property_mapper.types import LazyType

__all__ = ['ReelShare']


class ReelShare(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'tray': [LazyType('model.item.Item')],
        'story_ranking_token': str,
        'broadcasts': None,
        'sticker_version': int,
        'text': str,
        'type': str,
        'is_reel_persisted': bool,
        'reel_owner_id': int,
        'reel_type': str,
        'media': LazyType('model.item.Item'),
        'mentioned_user_id': int,
    }
