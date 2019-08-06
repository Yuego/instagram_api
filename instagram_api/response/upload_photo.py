from .base_response import Response

__all__ = ['UploadPhoteResponse']


class UploadPhoteResponse(Response):
    JSON_PROPERTY_MAP = {
        'upload_id': int,
        'media_id': int,
    }
