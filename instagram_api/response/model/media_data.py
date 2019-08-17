from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .image_versions2 import ImageVersions2
from .video_versions import VideoVersions

__all__ = ['MediaData', 'MediaDataInterface']


class MediaDataInterface(ApiInterfaceBase):
    image_versions2: ImageVersions2
    original_width: int
    original_height: int
    media_type: int
    video_versions: [VideoVersions]


class MediaData(PropertyMapper, MediaDataInterface):
    pass
