from instagram_api.property_mapper import PropertyMapperBase

from .direct_thread import DirectThread

__all__ = ['DirectInbox']


class DirectInbox(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'has_older': bool,
        'unseen_count': int,
        'unseen_count_ts': None,
        'blended_inbox_enabled': bool,
        'oldest_cursor': None,
        'threads': [DirectThread],
    }
