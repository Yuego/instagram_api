from .base_response import Response
from .model import VideoUploadUrl

__all__ = ['UploadJobVideoResponse']


class UploadJobVideoResponse(Response):
    JSON_PROPERTY_MAP = {
        'upload_id': int,
        'video_upload_urls': [VideoUploadUrl],
    }
