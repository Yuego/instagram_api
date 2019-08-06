from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['Surface']


class Surface(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'scores': None,
        'rank_token': str,
        'ttl_secs': int,
        'name': str,
    }
