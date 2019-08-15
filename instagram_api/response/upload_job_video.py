from .base_response import ApiResponse
from .model import VideoUploadUrl

__all__ = ['UploadJobVideoResponse']


class UploadJobVideoResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'upload_id': int,
        'video_upload_urls': [VideoUploadUrl],
    }
