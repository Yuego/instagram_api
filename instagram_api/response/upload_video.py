from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['UploadVideoResponse']


class UploadVideoResponseInterface(ApiResponseInterface):
    upload_id: str
    configure_delay_ms: float
    result: AnyType


class UploadVideoResponse(ApiResponse, UploadVideoResponseInterface):
    pass
