from instagram_api.property_mapper import PropertyMapperBase

from .direct_reaction import DirectReaction

__all__ = ['DirectReactions']


class DirectReactions(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'likes_count': int,
        'likes': [DirectReaction]
    }
