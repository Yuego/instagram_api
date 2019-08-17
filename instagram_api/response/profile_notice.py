from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['ProfileNoticeResponse']


class ProfileNoticeResponseInterface(ApiResponseInterface):
    has_change_password_megaphone: bool


class ProfileNoticeResponse(ApiResponse, ProfileNoticeResponseInterface):
    pass
