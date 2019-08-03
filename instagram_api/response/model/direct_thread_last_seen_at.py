from instagram_api.property_mapper import PropertyMapperBase
from instagram_api.property_mapper.types import timestamp

__all__ = ['DirectThreadLastSeenAt']


class DirectThreadLastSeenAt(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'item_id': int,
        'timestamp': timestamp,
    }
