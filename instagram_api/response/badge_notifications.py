from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model.unpredictable import CoreUnpredictableContainer

__all__ = ['BadgeNotificationsResponse']


class BadgeNotificationsResponseInterface(ApiResponseInterface):
    badge_payload: CoreUnpredictableContainer


class BadgeNotificationsResponse(ApiResponse, BadgeNotificationsResponseInterface):
    pass
