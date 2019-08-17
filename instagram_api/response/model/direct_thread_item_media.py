from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .audio_context import AudioContext
from .image_versions2 import ImageVersions2
from .video_versions import VideoVersions

__all__ = ['DirectThreadItemMedia', 'DirectThreadItemMediaInterface']


class DirectThreadItemMediaInterface(ApiInterfaceBase):
    media_type: int
    image_versions2: ImageVersions2
    video_versions: [VideoVersions]
    original_width: int
    original_height: int
    audio: AudioContext


class DirectThreadItemMedia(PropertyMapper, DirectThreadItemMediaInterface):
    PHOTO = 1
    VIDEO = 2
    AUDIO = 11
