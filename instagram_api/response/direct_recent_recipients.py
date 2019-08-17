from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['DirectRecentRecipientsResponse']


class DirectRecentRecipientsResponseInterface(ApiResponseInterface):
    expiration_interval: AnyType
    recent_recipients: AnyType


class DirectRecentRecipientsResponse(ApiResponse, DirectRecentRecipientsResponseInterface):
    pass
