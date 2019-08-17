from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['FacebookOTAResponse']


class FacebookOTAResponseInterface(ApiResponseInterface):
    bundles: AnyType
    request_id: str


class FacebookOTAResponse(ApiResponse, FacebookOTAResponseInterface):
    pass
