from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['ImageCandidate', 'ImageCandidateInterface']


class ImageCandidateInterface(ApiInterfaceBase):
    url: str
    width: int
    height: int
    estimated_scans_sizes: [int]


class ImageCandidate(PropertyMapper, ImageCandidateInterface):
    pass
