from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['Bold']


class Bold(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'start': int,
        'end': int,
    }
