from .base_response import ApiResponse

__all__ = ['UploadVideoResponse']


class UploadVideoResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'upload_id': str,
        'configure_delay_ms': float,
        'result': None,
    }
