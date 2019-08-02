from instagram_api.property_mapper import PropertyMapperBase
from instagram_api.property_mapper.types import timestamp

__all__ = ['DirectExpiringSummary']


class DirectExpiringSummary(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'type': str,
        'timestamp': timestamp,
        'count': int,
    }
