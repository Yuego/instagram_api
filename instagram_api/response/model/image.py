from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['Image']


class Image(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'uri': str,
        'width': int,
        'height': int,
    }
