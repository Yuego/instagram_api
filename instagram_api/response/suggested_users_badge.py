from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['SuggestedUsersBadgeResponse']


class SuggestedUsersBadgeResponseInterface(ApiResponseInterface):
    should_badge: AnyType
    new_suggestion_ids: [int]


class SuggestedUsersBadgeResponse(ApiResponse, SuggestedUsersBadgeResponseInterface):
    pass
