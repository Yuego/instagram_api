from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .image_candidate import ImageCandidate

__all__ = ['ImageVersions2', 'ImageVersions2Interface']


class ImageVersions2Interface(ApiInterfaceBase):
    candidates: [ImageCandidate]
    trace_token: AnyType


class ImageVersions2(PropertyMapper, ImageVersions2Interface):
    pass
