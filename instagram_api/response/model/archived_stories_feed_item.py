from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['ArchivedStoriesFeedItem']


class ArchivedStoriesFeedItem(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'timestamp': int,
        'media_count': int,
        'id': int,
        'reel_type': str,
    }
