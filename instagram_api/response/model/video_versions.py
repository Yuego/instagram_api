from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['VideoVersions', 'VideoVersionsInterface']


class VideoVersionsInterface(ApiInterfaceBase):
    type: int
    width: int
    height: int
    url: str
    id: int


class VideoVersions(PropertyMapper, VideoVersionsInterface):
    pass
