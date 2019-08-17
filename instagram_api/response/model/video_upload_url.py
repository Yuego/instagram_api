from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['VideoUploadUrl', 'VideoUploadUrlInterface']


class VideoUploadUrlInterface(ApiInterfaceBase):
    url: str
    job: str
    expires: float


class VideoUploadUrl(PropertyMapper, VideoUploadUrlInterface):
    pass
