from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import VideoUploadUrl

__all__ = ['UploadJobVideoResponse']


class UploadJobVideoResponseInterface(ApiResponseInterface):
    upload_id: int
    video_upload_urls: [VideoUploadUrl]


class UploadJobVideoResponse(ApiResponse, UploadJobVideoResponseInterface):
    pass
