from .base_response import ApiResponse

__all__ = ['UploadPhoteResponse']


class UploadPhoteResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'upload_id': int,
        'media_id': int,
    }
