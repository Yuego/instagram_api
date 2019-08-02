from instagram_api.property_mapper import PropertyMapperBase

from .image_candidate import ImageCandidate
from .image_versions2 import ImageVersions2

__all__ = ['CoverMedia']


class CoverMedia(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'id': int,
        'media_id': int,

        'media_type': int,
        'image_versions2': ImageVersions2,
        'original_width': int,
        'original_height': int,
        'cropped_image_version': ImageCandidate,
        'crop_rect': [int],
        'full_image_version': ImageCandidate,
    }
