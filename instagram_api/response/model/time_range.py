from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['TimeRange']


class TimeRange(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'start': int,
        'end': int,
    }
