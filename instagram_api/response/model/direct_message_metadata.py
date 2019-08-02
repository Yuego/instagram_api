from instagram_api.property_mapper import PropertyMapperBase
from instagram_api.property_mapper.types import timestamp

__all__ = ['DirectMessageMetadata']


class DirectMessageMetadata(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'thread_id': int,
        'item_id': int,
        'timestamp': timestamp,
        'participant_ids': [int],
    }
