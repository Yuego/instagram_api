from instagram_api.property_mapper import PropertyMapperBase

from .audio_context import AudioContext
from .image_versions2 import ImageVersions2
from .video_versions import VideoVersions

__all__ = ['DirectThreadItemMedia']


class DirectThreadItemMedia(PropertyMapperBase):
    PHOTO = 1
    VIDEO = 2
    AUDIO = 11

    JSON_PROPERTY_MAP = {
        'media_type': int,
        'image_versions2': ImageVersions2,
        'video_versions': [VideoVersions],
        'original_width': int,
        'original_height': int,
        'audio': AudioContext,
    }
