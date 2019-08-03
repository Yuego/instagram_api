from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['Explore']


class Explore(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'explanation': None,
        'actor_id': int,
        'source_token': None,
    }
