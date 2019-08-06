from instagram_api.property_mapper import PropertyMapperBase
from instagram_api.property_mapper.types import LazyType

__all__ = ['Channel']


class Channel(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'channel_id': int,
        'channel_type': None,
        'title': None,
        'header': None,
        'media_count': int,
        'media': LazyType('model.item.Item'),
        'context': None,
    }
