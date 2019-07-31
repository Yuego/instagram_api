from instagram_api.property_mapper import PropertyMapperBase

from .user import User

__all__ = ['BroadcastQuestion']


class BroadcastQuestion(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'text': str,
        'qid': str,
        'source': str,
        'user': User,
        'story_sticker_text': str,
        'timestamp': str,
    }
