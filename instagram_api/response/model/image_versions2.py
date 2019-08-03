from instagram_api.property_mapper import PropertyMapperBase

from .image_candidate import ImageCandidate

__all__ = ['ImageVersions2']


class ImageVersions2(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'candidates': [ImageCandidate],
        'trace_token': None,
    }
