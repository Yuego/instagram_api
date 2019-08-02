from instagram_api.property_mapper import PropertyMapperBase
from instagram_api.property_mapper.types import timestamp

__all__ = ['DirectReaction']


class DirectReaction(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'reaction_type': str,
        'timestamp': timestamp,
        'sender_id': int,
        'client_context': str,
        'reaction_status': str,
        'node_type': str,
        'item_id': int,
    }
