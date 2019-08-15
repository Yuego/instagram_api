from .base_response import ApiResponse

__all__ = ['BadgeNotificationsResponse']


class BadgeNotificationsResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'badge_payload': 'Model\UnpredictableKeys\CoreUnpredictableContainer',
    }
