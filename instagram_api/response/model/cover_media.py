from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .image_candidate import ImageCandidate
from .image_versions2 import ImageVersions2

__all__ = ['CoverMedia', 'CoverMediaInterface']


class CoverMediaInterface(ApiInterfaceBase):
    id: int
    media_id: int

    media_type: int
    image_versions2: ImageVersions2
    original_width: int
    original_height: int
    cropped_image_version: ImageCandidate
    crop_rect: [int]
    full_image_version: ImageCandidate


class CoverMedia(PropertyMapper, CoverMediaInterface):
    pass
