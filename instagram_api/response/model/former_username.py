from instagram_api.property_mapper import PropertyMapperBase
from instagram_api.property_mapper.types import timestamp

__all__ = ['FormerUsername']


class FormerUsername(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'former_username': str,
        'change_timestamp': timestamp,
    }
