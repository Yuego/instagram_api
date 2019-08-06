from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['VideoUploadUrl']


class VideoUploadUrl(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'url': str,
        'job': str,
        'expires': float,
    }
