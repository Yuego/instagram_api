from .base_response import ApiResponse

__all__ = ['ResumableUploadResponse']


class ResumableUploadResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'xsharing_nonces': None,
        'upload_id': int,
    }
