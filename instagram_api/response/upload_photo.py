from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['UploadPhotoResponse']


class UploadPhotoResponseInterface(ApiResponseInterface):
    upload_id: int
    media_id: int


class UploadPhotoResponse(ApiResponse, UploadPhotoResponseInterface):
    pass
