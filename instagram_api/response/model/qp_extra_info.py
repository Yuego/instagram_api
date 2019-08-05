from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['QPExtraInfo']


class QPExtraInfo(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'surface': int,
        'extra_info': str,
    }
