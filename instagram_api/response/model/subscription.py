from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['Subscription']


class Subscription(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'topic': None,
        'url': str,
        'sequence': None,
        'auth': None,
    }
