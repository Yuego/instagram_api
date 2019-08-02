from instagram_api.property_mapper import PropertyMapperBase
from instagram_api.property_mapper.types import timestamp

__all__ = ['DirectSeenItemPayload']


class DirectSeenItemPayload(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'count': int,
        'timestamp': timestamp,
    }
