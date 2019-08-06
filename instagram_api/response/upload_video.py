from .base_response import Response

__all__ = ['UploadVideoResponse']


class UploadVideoResponse(Response):
    JSON_PROPERTY_MAP = {
        'upload_id': str,
        'configure_delay_ms': float,
        'result': None,
    }
