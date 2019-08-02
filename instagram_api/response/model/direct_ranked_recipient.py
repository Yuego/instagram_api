from instagram_api.property_mapper import PropertyMapperBase

from .direct_thread import DirectThread
from .user import User

__all__ = ['DirectRankedRecipient']


class DirectRankedRecipient(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'thread': DirectThread,
        'user': User,
    }
