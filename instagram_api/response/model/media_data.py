from instagram_api.property_mapper import PropertyMapperBase

from .image_versions2 import ImageVersions2
from .video_versions import VideoVersions

__all__ = ['MediaData']


class MediaData(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'image_versions2': ImageVersions2,
        'original_width': int,
        'original_height': int,
        'media_type': int,
        'video_versions': [VideoVersions],
    }
