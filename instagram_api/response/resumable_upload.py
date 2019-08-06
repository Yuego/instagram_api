from .base_response import Response

__all__ = ['ResumableUploadResponse']


class ResumableUploadResponse(Response):
    JSON_PROPERTY_MAP = {
        'xsharing_nonces': None,
        'upload_id': int,
    }
