from instagram_api.property_mapper import PropertyMapperBase
from instagram_api.property_mapper.types import timestamp

__all__ = ['DirectSendItemPayload']


class DirectSendItemPayload(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'client_request_id': int,
        'client_context': str,
        'message': str,
        'item_id': int,
        'timestamp': timestamp,
        'thread_id': int,
        'canonical': bool,
        'participant_ids': [int],
    }
