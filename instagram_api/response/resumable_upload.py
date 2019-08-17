from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['ResumableUploadResponse']


class ResumableUploadResponseInterface(ApiResponseInterface):
    xsharing_nonces: AnyType
    upload_id: int


class ResumableUploadResponse(ApiResponse, ResumableUploadResponseInterface):
    pass
