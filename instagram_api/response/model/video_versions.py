from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['VideoVersions']


class VideoVersions(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'type': int,
        'width': int,
        'height': int,
        'url': str,
        'id': int,
    }
